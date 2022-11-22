Welcome to the **LSA SAF data service**.

For queries, contact helpdesk.landsaf@ipma.pt 

Check this <a href="https://gitlab.com/helpdesk.landsaf/lsasaf_data_access" target="_blank">git repository</a> for tips to access the data. 

The recomended way to download several products is with the [**wget**](https://www.gnu.org/software/wget/ 
) tool which is available in most linux distributions. For windows details will be included

For example to download MSG LST hourly files (skipping minutes 15, 30, 45) for Jan 2006 you can use the following command (don’t forget the last “/” to download only that period) (replace --user=XXX --password=XXX by your access credentials):
```
wget -c --no-check-certificate -r -np -nH \
     --user=XXX --password=XXX \
     -R "*15.nc, *30.nc, *45.nc, *.html" \
     https://datalsasaf.lsasvcs.ipma.pt/PRODUCTS/MSG/MLST/NETCDF/2006/01/
```
You can check the details of each option [here](https://www.gnu.org/software/wget/manual/wget.html). If you add the option “-nd” all files are saved to the current directly, otherwise they will be downloaded to a folder structure PRODUCTS/MSG/MLST/NETCDF/2006/01/

**Data organization**

The data is organized as:

 `https://datalsasaf.lsasvcs.ipma.pt/PRODUCTS/<satellite>/<product>/<format>/<year>/<month>/<day>/filename`

[satellite](#satellite): satellite missions: EPS, MSG, MSG-IODC  
[product](#product): See [below](#product) the list of products  
format: Data format: NETCDF, HDF5  
year/month/day: year with 4 digits, month with 2 digits, day with two digits 


<a name="satellite"></a>
**Satellite missions**

**EPS**: Metop polar orbiting meteorological satellites of the EUMETSAT Polar System

**MSG**: Meteosat Second Generation, geostationary  at 0 degrees East 

**MSG-IOCD**: Meteosat Second Generation, geostationary at 41.5/45.5 degrees East Indian Ocean Data Coverage 


<a name="product"></a>
**Products acronyms**   
<table>
  <tr>
    <th>Acronym</th> <th>Description</th> <th>Satellite missions</th> <th>Format</th>
  </tr>
 
  <tr> <td colspan="4"><b>Land Surface temperature and emissivity</b></td> </tr>
  <tr> <td>DLST</td> <td>Derived LST: 10-day composites</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MEM</td> <td>Land Surface Emissivity</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MLST</td> <td>Land Surface Temperature</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MLST-AS</td> <td>Land Surface Temperature - All Sky</td> <td>MSG</td> <td>HDF5, NETCDF</td>
  <tr> <td>EDLST</td> <td>Daily Land Surface Temperature</td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td colspan="4"><b>Fire</b></td> </tr>
  <tr> <td>FRP-GRID</td> <td>Fire Radiative Power Gridded</td> <td>MSG</td> <td>HDF5</td> </tr>
  <tr> <td>FRP-PIXEL</td> <td>Fire Radiative Power Pixel</td> <td>MSG, MSG-IODC</td> <td>HDF5</td> </tr>
  <tr> <td>FRMv2</td> <td>Fire Risk Map version 2</td> <td>MSG</td> <td>HDF5</td> </tr>

  <tr> <td colspan="4"><b>Albedo and Vegetation</b></td> </tr>
  <tr> <td>MDAL</td> <td>Daily Surface Albedo</td> <td>MSG, MSG-IOCD</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MDFAPAR</td> <td>Daily Fraction of Absorved Photosynthetic Active Radiation</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MDFVC</td> <td>Daily Fraction of Vegetation Cover</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MDLAI</td> <td>Daily Leaf Area Index</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MGPP</td> <td>10-days Gross Primary Production</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MTAL</td> <td>10-day Surface Albedo</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MTFAPAR</td> <td>10-day Fraction of Absorved Photosynthetic Active Radiation</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MTVFC</td> <td>10-day Fraction of Vegetation Cover</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MTLAI</td> <td>10-day Leaf Area Index</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>ETAL</td> <td>10-day Surface Albedo</td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>ETFAPAR</td> <td>10-day Fraction of Absorved Photosynthetic Active Radiation</td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>ETFVC</td> <td>10-day Fraction of Vegetation Cover</td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>ETLAI</td> <td>10-day Leaf Area Index</td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>

  <tr> <td colspan="4"><b>Radiation fluxes</b></td> </tr>
  <tr> <td>MDIDSLF</td> <td>Daily Downward Surface Longwave Flux</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MDIDSSF</td> <td>Daily Downward Surface Shortwave Flux</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MDSLF</td> <td>Downward Surface Longwave Flux</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MDSSFTD</td> <td>Total and Diffuse Downward Surface Shortwave Flux</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td>MNSLF</td> <td>Net Surface Longwave</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td colspan="4"><b>Evaporation and turbulent fluxes</b></td> </tr> <tr> 
  <tr> <td> METREF</td> <td>Reference Evapotranspiration</td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td> MDMET</td> <td>Daily Evapotranspiration</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td> MET</td> <td>Evapotranspiration</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td> MH</td> <td>Sensible heat flux</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  <tr> <td> MLE</td> <td>Latent heat flux</td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  

  <tr> <td colspan="4"><b>HSAF products</b></td> </tr> 
  <tr> <td>MDSC</td> <td>Daily snow cover (HSAF H31)</td> <td>MSG</td> <td>HDF5</td> </tr>
  <tr> <td>EDSC</td> <td>Daily Snow Cover (HSAF H32)</td> <td>EPS</td> <td>HDF5</td> </tr>  
  
</table>

**Disclaimer**:<br> All intellectual property rights of the LSA SAF products belong to EUMETSAT. The use of these products is granted to every interested user, free of charge. If you wish to use these products, EUMETSAT's copyright credit must be shown by displaying the words "copyright (year) EUMETSAT" on each of the products used.
