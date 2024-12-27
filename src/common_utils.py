import datetime as dt
import thredds_lsasaf_utils as tlu
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import rasterio
from rasterio.mask import mask
from shapely import wkt

import statsmodels.api as sm
from statsmodels.genmod.families import Gaussian
from statsmodels.genmod.families.links import Power
from statsmodels.genmod.families import Gamma
from statsmodels.genmod.families.links import log, identity

import pickle
import os
import thredds_lsasaf_utils as tlu

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.genmod.families import Gaussian
from statsmodels.genmod.families.links import Power
from statsmodels.genmod.families import Gamma
from statsmodels.genmod.families.links import log, identity

import pickle

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import patsy

# Match points and add columns
def add_landuse_to_gdf(gdf, landuse_profile):

    # Initialize an empty dictionary to store land use proportions for each point
    landuse_data = []
    for _, row in gdf.iterrows():
        point = row.geometry  # Get the point geometry
        # Retrieve land use proportions for the point
        proportions = landuse_profile.get(point, {col: 0 for col in next(iter(landuse_profile.values())).keys()})
        landuse_data.append(proportions)

    # Convert the land use data into a DataFrame
    landuse_df = pd.DataFrame(landuse_data)

    # Concatenate with the original GeoDataFrame
    gdf = pd.concat([gdf, landuse_df], axis=1)

    return gdf


def read_fused_data(filename):

    # Replace 'your_file.csv' with the path to your CSV file
    file_path = filename

    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Ensure the CSV contains 'lat' and 'lon' columns
    if 'lat' not in df.columns or 'lon' not in df.columns:
        raise ValueError("The CSV file must contain 'lat' and 'lon' columns")

    # Create a GeoDataFrame
    geometry = [Point(xy) for xy in zip(df['lon'], df['lat'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry)

    # Set the coordinate reference system (CRS) if known, e.g., WGS84 (EPSG:4326)
    gdf.set_crs(epsg=4326, inplace=True)

    return gdf


def round_geometry(geom, precision=6):
    '''# Round coordinates to a consistent precision (e.g., 6 decimal places)'''

    # Ensure it's a Point geometry and apply rounding to x and y coordinates
    if isinstance(geom, Point):
        return Point(round(geom.x, precision), round(geom.y, precision))
    return geom  # If it's not a Point, return it as-is (can be extended to other geometries)


def add_land_use(csv_filename, landuse_pickle_filename, destination_dir):

    # Read the .csv file into a geopandas df
    gdf = read_fused_data(csv_filename)

    # Load the pickle file
    with open(landuse_pickle_filename, 'rb') as file:
        loaded_geo_lulc_dict = pickle.load(file)

    # Round the geometries in the dictionary to 6 decimal places
    loaded_geo_lulc_dict = {
        round_geometry(key): value for key, value in loaded_geo_lulc_dict.items()
    }

    # Update GeoDataFrame geometry
    gdf['geometry'] = gdf['geometry'].apply(lambda geom: round_geometry(geom))

    sample_point = gdf['geometry'].iloc[0]
    print("Sample GeoDataFrame Point:", sample_point)
    print("Is this point in the dictionary?", sample_point in loaded_geo_lulc_dict)

    # Add land use data to GeoDataFrame
    gdf_with_landuse = add_landuse_to_gdf(gdf, loaded_geo_lulc_dict)

    return gdf_with_landuse


def save_lst_gdf(gdf, destination_dir, csv_filename):

    columns_to_keep = ['time', 'lat', 'lon', 'temperature', 'hour', 'day', 'month', 'year',
       'geometry', 'water', 'trees', 'flooded_veg', 'crop', 'built_area',
       'bare_ground', 'range_land']

    # Retain only the specified columns
    gdf = gdf.loc[:, columns_to_keep]

    print(type(gdf['geometry'].iloc[0]))

    # Convert geometry to WKT format
    # gdf['geometry'] = gdf['geometry'].apply(lambda geom: geom.wkt)

    # Create destination_dir if it does not exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Save to CSV
    output_csv_path = os.path.join(destination_dir, f'lu_fused_{csv_filename}')
    gdf.to_csv(output_csv_path, index=False)

    print(f"GeoDataFrame saved to {output_csv_path}")


def glm_model(gdf, interaction_formula):

    # Define target and LULC columns
    target = 'temperature'  # Replace with your target column name

    # Ensure categorical variables are treated as such
    gdf['hour'] = gdf['hour'].astype('category')
    gdf['month'] = gdf['month'].astype('category')
    gdf['year'] = gdf['year'].astype('category')

    # Drop the geometry column
    gdf = gdf.drop(columns=['geometry'])

    # Define LULC columns (all columns except the target)
    lulc_columns = ['water', 'trees', 'flooded_veg', 'crop', 'built_area', 'bare_ground', 'range_land']

    # Drop rows with missing values
    gdf = gdf.dropna(subset=[target, 'hour', 'month', 'year'] + lulc_columns)

    # Step 2: Split the data into training and testing
    train_data, test_data = train_test_split(gdf, train_size=0.75, test_size=0.25)

    import statsmodels.api as sm

    # Step 3: Generate design matrices for train and test sets
    y_train, X_train = patsy.dmatrices(interaction_formula, data=train_data, return_type='dataframe')
    y_test, X_test = patsy.dmatrices(interaction_formula, data=test_data, return_type='dataframe')

    # Step 4: Fit the GLM model on the training data
    gamma_model = sm.GLM(y_train, X_train, family=sm.families.Gamma(link=sm.families.links.log()))
    gamma_results = gamma_model.fit()

    # Step 5: Display model summary
    print(gamma_results.summary())

    # Make predictions on the test data
    y_pred = gamma_results.predict(X_test)

    # Plot observed vs predicted values
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.7, edgecolors='k', label='Data points')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', label='Perfect Fit')
    plt.xlabel("Observed Temperature")
    plt.ylabel("Predicted Temperature")
    plt.title("Observed vs Predicted Temperature")
    plt.legend()
    plt.grid(True)
    plt.show()

    return gamma_results
