![Course banner](./img/banner.png)

# LSA SAF PRODUCTS CASE STUDIES

[![Python](https://img.shields.io/badge/python-anaconda-blue)](https://www.anaconda.com/products/distribution)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE.txt)

<hr>

## Description


This **repository** module consists of a collection of Python-based Jupyter Notebooks (JNs) designed to demonstrate applications of the LSA SAF (Satellite Application Facility on Land Surface Analysis) products.
The module contains some introductory notebooks for basic plotting and analysis of satellite-based data as well as comparison with in-situ meteorological observations. 

For any questions about this repository, please contact helpdesk.landsaf@ipma.pt.

## License

This code is licensed under an MIT license. See file LICENSE.txt for details on 
the usage and distribution terms. No dependencies are distributed as part of this 
package. Copyright EUMETSAT 2024.

All product names, logos, and brands are the property of their respective owners. 
All company, product and service names used in this website are for identification 
purposes only.

## Authors

* [**Vid Primožič**](mailto://helpdesk.landsaf@ipma.pt) - [ARSO](https://www.arso.si) - [LSA SAF](https://www.lsa-saf.eumetsat.int)
* [**Ahac Pazlar**](mailto://helpdesk.landsaf@ipma.pt) - [ARSO](https://www.arso.si) - [LSA SAF](https://www.lsa-saf.eumetsat.int)
* [**Boštjan Muri**](mailto://helpdesk.landsaf@ipma.pt) - [ARSO](https://www.arso.si) - [LSA SAF](https://www.lsa-saf.eumetsat.int)

Please see the `AUTHORS.txt` file for more information on contributors.
<hr>


## Case Studies Outline

This case studies are split in four groups LST, VEGA, ETP and DSSF:


* LST/01_MLST_plot_NetCDF4.ipynb:  
 **title:** [Displaying LSA SAF MLST with cartopy and xarray](LST/01_MLST_plot_NetCDF4.ipynb)
>
> This Jupyter Notebook presents opening and plotting LSA SAF MLST products in `NetCDF4` file format. LSA SAF MLST product for August 21, 2023, is Plotted in Plate-Carree and Robinson geographical projection.

* LST/02_MLST_data_quality.ipynb:  
 **title:** [Analysing Uncertainty of LSA SAF MLST Product](LST/02_MLST_data_quality.ipynb)
>
> This Jupyter Notebook presents the investigation of the LSA SAF MLST product's standard error and quality flag estimates. LSA SAF MLST product standard error and quality flag are plotted for August 21, 2023, in Lambert conformal geostationary projection.
> 
* LST/03_Plot_Land_temperature_comparison.ipynb:  
 **title:** [Comparison Between LSA-SAF MLST-ASv2, Air Temperature Measurements](LST/03_Plot_Land_temperature_comparison.ipynb)
>
> This Jupyter Notebook presents the analysis of the LSA SAF MLST-ASv2 product and its comparison with the in-situ measurements of the 2m air temperature. LSA SAF MLST-ASv2 product is an estimate for land surface temperature, based on the observations of the Meteosat Second Generation satellite. The 2m air temperature is connected to the land surface temperature and this JN aims to compare measurements of mentioned quantities.

* LST/04_Plot_anomaly.ipynb:  
 **title:** [Plotting the Maximum Daily Temperature Anomaly](LST/04_Plot_anomaly.ipynb)
>
> This Jupyter Notebook presents the preparation of the animation of the maximum daily land surface temperature anomaly calculated from the LSA SAF MLST-ASv2 and pre-calculated reference available on the LSA SAF Data Server for the period July 1, 2023, to August 31, 2023. Animation is exported as a GIF.

* VEGA/05_Vegetation_products.ipynb:  
 **title:** [Demonstration of Meteosat Second Generation Satellite Based LSA SAF Vegetation Products](VEGA/05_Vegetation_products.ipynb)
>
> This JN demonstrates the use of LSA SAF MDFAPAR, LSA SAF MDLAI and LSA SAF MDFVC products. Plotting of locally saved data and accessing the data on the LSA SAF THREDDS Data Server are shown as well as production of GIF animation.

* VEGA/06_Vegetation_anomaly_THREDDS.ipynb:  
 **title:** [Calculation of Fractional Vegetation Cover anomaly (FVC) from ETFVC product](VEGA/06_Vegetation_anomaly_THREDDS.ipynb)
>
> This JN presents the calculation of FVC anomaly from the LSA SAF ETFVC product for the period from January 1, 2022, to December 31, 2022. The product data are accessed from the LSA SAF THREDDS Data Server.

* VEGA/07_Vegetation_anomaly.ipynb:  
 **title:** [Calculation of Fractional Vegetation Cover anomaly (FVC) based on LSA SAF ETFVC product using locally saved data](VEGA/07_Vegetation_anomaly.ipynb)
>
> This JN presents the calculation of the fraction of vegetation cover anomaly for year the 2022 based on the LSA SAF ETFVC product. FVC anomaly is calculated based on locally saved data.

* VEGA/08_Wild_fire_analysis.ipynb:  
 **title:** [Analysing the Effects of Wild Fires on Vegetation Using LSA SAF MSG MDFVC Product and LSA SAF MSG-FRP Pixel Product](VEGA/08_Wild_fire_analysis.ipynb)
>
> This JN demonstrates the effect of wildfires on FVC. LSA SAF FRP product is used to show the firepower in the affected area and a change of LSA SAF FVC value is used to demonstrate the effect of fire on vegetation.

* ETP/09_Discrepancy_METREF_DMETv3:  
 **title:** [Indicating Water Deficit with the Discrepancy Between Actual and Reference Evapotranspiration](ETP/09_Discrepancy_METREF_DMETv3)
>
> This Jupyter Notebook presents the calculation of the difference between LSA SAF METREF and LSA SAF DMETv3 product. This difference can be used as an indicator of water deficit.

* ETP/10_METREF_In_Situ_ET_Comparison.ipynb:  
 **title:** [Comparing LSA SAF METREF Data with Evapotranspiration Estimates Based on In-situ Measurement](ETP/10_METREF_In_Situ_ET_Comparison.ipynb)
>
> This JN presents a comparison of LSA SAF METREF product estimation for evapotranspiration with estimations obtained using the Penman-Montith formula based on in-situ measurements. Comparison is made for 3 locations in Slovenia with external evapotranspiration estimates provided by ARSO.


* DSSF/11_Solar_radiation_chart.ipynb:  
 **title:** [Calculating the Average MDSSFTD Values and Investigating the Sky Conditions in the First Decade of April 2024](DSSF/11_Solar_radiation_chart.ipynb)
>
> This notebook demonstrates the calculation of average DSSF from LSA SAF MDSSFTD product and demonstrates the efect of cloud conditions of the average total DSSF values.

* DSSF/12_Acquisition_time_analysis.ipynb:  
 **title:** [Comparing LSA SAF METREF Data with Evapotranspiration Estimates Based on In-situ Measurements](DSSF/11_Solar_radiation_chart.ipynb)
>
> This Jupyter notebook presents comparison of MDSSFTD with in-situ for 2 locations Payerne in Central Europe and Tamanrasset in North Africa.


## Getting Started

These instructions will help you to set up material on your local machine and run the notebooks.

### Environment Requirements

You will require [Jupyter](https://jupyter.org) to run this code.
It is an open-source application that allows us to create documents for high-level interactive learning by allowing us to combine code, text description and data visualisations. 

#### Dependencies

JNs presented here require `Python` as well as [`Jupyter`](https://jupyter.org/) or [`Jupyter-lab`](https://jupyter.org/) and several other dependencies that are not included but are required:

|item|version|licence|package info|
|---|---|---|---|
|jupyterlab|4.1.6|BSD-3-Clause|https://anaconda.org/conda-forge/jupyterlab|
|dask|2024.4.1|BSD-3-Clause|https://anaconda.org/conda-forge/dask|
|xarray|2024.3.0|Apache-2.0|https://anaconda.org/conda-forge/xarray|
|netcdf4|1.6.5|MIT|https://anaconda.org/conda-forge/netcdf4|
|scipy|1.13.0|BSD-3-Clause|https://anaconda.org/conda-forge/scipy|
|matplotlib|3.8.4|PSF-2.0|https://anaconda.org/conda-forge/matplotlib|
|cartopy|0.23.0|BSD-3-Clause|https://anaconda.org/conda-forge/cartopy|
|h5py|3.11.0|BSD-3-Clause|https://anaconda.org/conda-forge/h5py|
|tqdm|4.66.2|MPL-2.0 or MIT|https://anaconda.org/conda-forge/tqdm|
|shapely|2.0.4|BSD-3-Clause|https://anaconda.org/conda-forge/shapely|
|pandas|2.2.2|BSD-3-Clause|https://anaconda.org/conda-forge/pandas|

#### Environment Setup

You can **clone this repo** and run the notebooks on your local machine.
If no other option is preferred, we suggest the installation of the [conda](https://docs.conda.io/projects/conda/en/stable/index.html), since it works on various platforms (Linux, Windows, macOS). To install conda and set up a virtual environment:

* [1. - Download and install conda](https://docs.conda.io/projects/conda/en/stable/index.html)
* [2. - Once in `conda` create a virtual environment from the `environment.yml` file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

```
conda env create -f environment.yml
```
`Jupyter` is already included in `environment.yml` so no other actions are needed.

This will create a Python environment. The environment won't be activated by default.
* [3. - To activate virtual environment run](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment).

```
conda activate environment_name
```
Envrironment name is written at the top of environemnt.yml file. 

*Note: remember that you may need to reactivate the conda environment in every newly created window instance*


### Usage of the Jupyter Notebooks

JNs are a set of markdown and code cells. To use notebooks ensure that the right environment is activated, then follow the next steps:

* [1. - Run `jupyter notebook` or `jupyter lab`](https://docs.jupyter.org/en/latest/running.html) from the directory with the notebook:

```
jupyter notebook <name-of-notebook.ipynb>
```
or:

```
jupyter-lab
```
The `jupyter-lab` offers some additional tools and features for working with notebooks.

This should open JN in a browser window.
If not, then paste the given URL from terminal to browser.

* [2. - Basic use of Jupyter Notebooks editor and basic commands is described here](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html).


