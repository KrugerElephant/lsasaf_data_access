<div style="text-align: center;">
<img src="https://lsa-saf.eumetsat.int/static/logo.png">
</div>

 
## Welcome to the **LSA SAF data service**.


For queries, contact helpdesk.landsaf@ipma.pt 

### Data access

Access to the files in the data archive is restricted to registered users.<br>
<b><a href="https://mokey.lsasvcs.ipma.pt/auth/signup" target="_blank">Register here</a></b> / 
<b><a href="https://mokey.lsasvcs.ipma.pt/auth/forgotpw" target="_blank">Reset password</a></b>

<b><a href="https://gitlab.com/helpdesk.landsaf/lsasaf_data_access/-/wikis/home" target="_blank">Data Service User Guide</a></b>

<details>
  <summary><b>Click for some examples </b> </summary>


**https / wget**

The recomended way to download several products is with the [**wget**](https://www.gnu.org/software/wget/ 
) tool which is available in most linux distributions. Windows binaries can be found [here](https://eternallybored.org/misc/wget/)

For example to download MSG LST hourly files (skipping minutes 15, 30, 45) for Jan 2006 you can use the following command (don’t forget the last “/” to download only that period) (replace --user=XXX --password=XXX by your access credentials):
```
wget -c --no-check-certificate -r -np -nH \
     --user=XXX --password=XXX \
     -R "*15.nc, *30.nc, *45.nc, *.html" \
     https://datalsasaf.lsasvcs.ipma.pt/PRODUCTS/MSG/MLST/NETCDF/2006/01/
```
You can check the details of each option [here](https://www.gnu.org/software/wget/manual/wget.html). If you add the option “-nd” all files are saved to the current directly, otherwise they will be downloaded to a folder structure PRODUCTS/MSG/MLST/NETCDF/2006/01/

**WebDAV**

WebDAV protocol is the recomended way to access the files directly from Windows, using "map a network drive"

Details <a href="https://gitlab.com/helpdesk.landsaf/lsasaf_data_access/-/wikis/data/webdav" target="_blank">here</a> and ipython notebook examples <a href="https://gitlab.com/helpdesk.landsaf/lsasaf_data_access/-/tree/main/examples/webdav" target="_blank">here</a>. 

**THREDDS**

THREDDS/OpenDAP protocol is the recommended way to access NETCDF files to subset regions/variables. 

Details <a href="https://gitlab.com/helpdesk.landsaf/lsasaf_data_access/-/wikis/data/thredds" target="_blank">here</a> and ipython notebook examples <a href="https://gitlab.com/helpdesk.landsaf/lsasaf_data_access/-/tree/main/examples/thredds" target="_blank">here</a>. 

Examples of command line tools to access directly the files via OpenDAP (replace "USER:PASSWD" by your credentials).

```
# netcdf header
ncdump -h https://USER:PASSWD@thredds.lsasvcs.ipma.pt/thredds/dodsC/EPS/ETLAI/NETCDF/2020/02/15/NETCDF4_LSASAF_M01-AVHR_ETLAI_GLOBE_202002150000.nc
# cdo short information
cdo sinfov https://USER:PASSWD@thredds.lsasvcs.ipma.pt/thredds/dodsC/EPS/ETLAI/NETCDF/2020/02/15/NETCDF4_LSASAF_M01-AVHR_ETLAI_GLOBE_202002150000.nc


```


</details>

### Data organization

The data is organized as:

**HTTPS**: 
 `https://datalsasaf.lsasvcs.ipma.pt/PRODUCTS/<satellite>/<product>/<format>/<year>/<month>/<day>/filename`

**WEBDAV**: 
 `https://datalsasafwd.lsasvcs.ipma.pt/PRODUCTS/<satellite>/<product>/<format>/<year>/<month>/<day>/filename`

**THREDDS/OpenDAP (NETCDF ONLY)**
 ```
 https://thredds.lsasvcs.ipma.pt/thredds/catalog/catalog.html 
 <satellite>/<product>/<format>/<year>/<month>/<day>/filename
 ```

[**satellite**](#satellite): satellite missions: EPS, MSG, MSG-IODC  
[**product**](#product): See [below](#product) the list of products  
**format**: Data format: NETCDF, HDF5, ENVI (for EPS ENDVI10 only)  
year/month/day: year with 4 digits, month with 2 digits, day with two digits 


<a name="satellite"></a>
### Satellite missions

**EPS**: Metop polar orbiting meteorological satellites of the EUMETSAT Polar System

**MSG**: Meteosat Second Generation, geostationary  at 0 degrees East 

**MSG-IOCD**: Meteosat Second Generation, geostationary at 41.5/45.5 degrees East Indian Ocean Data Coverage 


<a name="product"></a>
### Products acronyms and organization

<table>
  <tr>
    <th>Acronym</th> <th>Description</th> <th>Satellite missions</th> <th>Format</th>
  </tr>
 <td >

 
  
  <tr> <td colspan="4" style="text-align: center"><b>
  <a href="https://landsaf.ipma.pt/en/data/products/land-surface-temperature-and-emissivity/" target="_blank">Land Surface temperature and emissivity </a></b></td> </tr>
  
  <tr> <td>MLST</td><td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/Dd6ga76oG7Lqz5Q" target="_blank">Land Surface Temperature</a> [15 min]
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MLST_DIR</td> <td>[LSA-004]</td> <td>2021-NRT</td> </tr>
  <tr> <td>MLST</td> <td>[LSA-001]</td> <td>2016-2021</td> </tr>
  <tr> <td>MLST-R</td> <td>[LSA-050]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MLST-AS</td><td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/dYjdyiMXZTt8sP4" target="_blank">Land Surface Temperature - All Sky</a>  [30 min]   
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MLST-AS</td> <td>[LSA-005]</td> <td>2020-NRT</td> </tr>
  </table>
  </td><td>MSG</td><td>HDF5, NETCDF</td>

  <tr> <td>MLST-ASv2</td><td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/DSnWj8n4gx3WQbm" target="_blank">Land Surface Temperature - All Sky version 2</a>
  [30 min] 
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MLST-ASv2</td> <td>[LSA-005.2]</td> <td>2004-NRT</td> </tr>
  </table>
  </td><td>MSG</td><td>HDF5, NETCDF</td>
  
  <tr> <td>DLST</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/yniroZGomKkDeXR" target="_blank">Derived LST: 10-day composites</a> 
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>DLST</td> <td>[LSA-003]</td> <td>2015-NRT</td> </tr>
  </table>
  </td><td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>EDLST</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/NsW275gpDAfekzc" target="_blank">Daily Land Surface Temperature</a> [day/night] 
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> EPS products info </td> </tr>
  <tr> <td>EDLST</td> <td>[LSA-002]</td> <td>2015-NRT</td> </tr>
  </table>
  </td><td>EPS</td><td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MEM</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/Dd6ga76oG7Lqz5Q" target="_blank">Daily Land Surface Emissivity</a>
  <br> MEM [DEMO] 2004-NRT 
  </td><td>MSG,MSG-IODC</td><td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MEMD</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/kxo9bs8QKGtytA3" target="_blank">Direct Emissivity Retrieval</a>
  [daily] <br> MEMD [LSA-006] 2004-NRT 
  </td><td>MSG</td><td>HDF5, NETCDF</td> </tr>
  

  <tr> <td colspan="4" style="text-align: center"><b>
  <a href="https://landsaf.ipma.pt/en/data/products/fire-products/" target="_blank">Wild Fires</a></b></td> </tr>
  
  <tr> <td>FRP-GRID</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/TjpsBziZFNN6GPN" target="_blank">Fire Radiative Power Gridded</a> [hourly]
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>FRPGrid</td> <td>[LSA-503]</td> <td>2016-NRT</td> </tr>
  <tr> <td>FRPGrid-R</td> <td>[LSA-551]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5</td> </tr>
  
  <tr> <td>FRP-PIXEL</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/TjpsBziZFNN6GPN" target="_blank">Fire Radiative Power Pixel</a> [15 min]
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>FRPPixel</td> <td>[LSA-502]</td> <td>2016-NRT</td> </tr>
  <tr> <td>FRPPixel-R</td> <td>[LSA-550]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5</td> </tr>

  <tr> <td>FREM</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/FarLHEfxKbgnGwQ" target="_blank">Fire Radiative Energy eMissions</a> [hourly/daily]
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>FREM</td> <td>[LSA-507]</td> <td>2004-NRT</td> </tr>
  </table>
  </td> <td>MSG</td> <td>NETCDF</td> </tr>
  
  <tr> <td>FRMv2</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/CjtrxjMcYBz5wT7" target="_blank">Fire Risk Map version 2</a> [daily] 
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>FRMv2</td> <td>[LSA-504.2]</td> <td>2021-NRT</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5</td> </tr>


  <tr> <td colspan="4" style="text-align: center"><b>
  <a href="https://landsaf.ipma.pt/en/data/products/albedo/" target="_blank">Albedo </a></b></td> </tr>
  
  <tr> <td>MDALv2</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/pApTpM4oaMnPZcM" target="_blank">Daily Surface Albedo version 2</a>
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDALv2</td> <td>[LSA-101.2]</td> <td>2004-NRT</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  
  <tr> <td>MTALv2</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/pApTpM4oaMnPZcM" target="_blank">10-day Surface Albedo version 2</a> [10 daily]
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MTALv2</td> <td>[LSA-102.2]</td> <td>2004-NRT</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MDAL</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/gFgGbMNQ2Gmns63" target="_blank">Daily Surface Albedo</a>
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDAL</td> <td>[LSA-101]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MDAL-R</td> <td>[DEMO]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IOCD</td> <td>HDF5, NETCDF</td> </tr>

  <tr> <td>MTAL</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/yWwSJ3ai2a7naHZ" target="_blank">10-day Surface Albedo</a>
   <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MTAL</td> <td>[LSA-102]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MTAL-R</td> <td>[LSA-150]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>


  <tr> <td>ETAL</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/6D4Q849exZRx3xW" target="_blank">10-day Surface Albedo</a>
  <br> 
  <table>
  <tr> <td>ETAL</td> <td>[LSA-103]</td>   <td>2021/07/05-NRT</td> </tr>
  <tr> <td>ETAL-R</td> <td>[LSA-152]</td> <td>2008-2021/06/25</td> </tr>
  </table>
  </td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  
  

  <tr> <td colspan="4" style="text-align: center"><b><a href="https://landsaf.ipma.pt/en/data/products/vegetation/" target="_blank">Vegetation </a></b></td> </tr>
  
  <tr> <td>MDFAPAR</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/LbAmqBTB3Q2tbQP" target="_blank">Daily Fraction of Absorved Photosynthetic Active Radiation</a>
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDFAPAR</td> <td>[LSA-425]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MDFAPAR</td> <td>[DEMO]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MDFVC</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/LbAmqBTB3Q2tbQP" target="_blank">Daily Fraction of Vegetation Cover</a>
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDFVC</td> <td>[LSA-421]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MDFVC</td> <td>[DEMO]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MDLAI</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/LbAmqBTB3Q2tbQP" target="_blank">Daily Leaf Area Index</a>
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDLAI</td> <td>[LSA-423]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MDAIL</td> <td>[DEMO]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MGPP</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/LNkWz498cA4Rf2Z" target="_blank">10-days Gross Primary Production</a>
  <br> 
  <table>
  <tr> <td>MGPP</td> <td>[LSA-411]</td> <td>2018-NRT</td> </tr>
  </table> 
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MTFAPAR</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/7co5rsXBqwR7kYg" target="_blank">10-day Fraction of Absorved Photosynthetic Active Radiation</a>
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MTFAPAR</td> <td>[LSA-426]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MTFAPAR-R</td> <td>[LSA-452]</td> <td>2004-2015</td> </tr>
  </table>  
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MTVFC</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/7co5rsXBqwR7kYg" target="_blank">10-day Fraction of Vegetation Cover</a>
   <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MTFVC</td> <td>[LSA-422]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MTFVC-R</td> <td>[LSA-450]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MTLAI</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/7co5rsXBqwR7kYg" target="_blank">10-day Leaf Area Index</a>
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MTLAI</td> <td>[LSA-424]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MTLAI-R</td> <td>[LSA-451]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>ETFAPAR</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/sWn23j9NZnJg2a6" target="_blank">10-day Fraction of Absorved Photosynthetic Active Radiation</a>
  <br> 
  <table>
  <tr> <td>ETFAPAR</td> <td>[LSA-409]</td> <td>2015-NRT</td> </tr>
  </table>  
  </td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>ETFVC</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/sWn23j9NZnJg2a6" target="_blank">10-day Fraction of Vegetation Cover</a>
  <br> 
  <table>
  <tr> <td>ETFVC</td> <td>[LSA-403]</td> <td>2015-NRT</td> </tr>
  </table>
  </td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>ETLAI</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/sWn23j9NZnJg2a6" target="_blank">10-day Leaf Area Index</a>
  <br> 
  <table>
  <tr> <td>ETLAI</td> <td>[LSA-406]</td> <td>2015-NRT</td> </tr>
  </table>
  </td> <td>EPS</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>ENDVI10</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/qqwZSwGC6mAHxZA" target="_blank">10-daily synthesis Normalized Difference Vegetation Index</a>
    <br> 
  <table>
  <tr> <td>ENDVI10</td> <td>[LSA-420]</td> <td>2020-NRT</td> </tr>
  <tr> <td>ENDVI10-R</td> <td>[LSA-454]</td> <td>2007-2019</td> </tr>
  </table>
  </td> <td>EPS</td> <td>ENVI</td> </tr>
  

  <tr> <td colspan="4" style="text-align: center"><b>
  <a href="https://landsaf.ipma.pt/en/data/products/radiation/" target="_blank">Surface Radiation</a></b></td> </tr>
  
  <tr> <td>MDSSFTD</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/bA9gYoa5mQX2yJw" target="_blank">Total and Diffuse Downward Surface Shortwave Flux</a> 15 min
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDSSFTD</td> <td>[LSA-207]</td> <td>2004-NRT</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MDSLF</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/m5X9LNMK9oAW55C" target="_blank">Downward Surface Longwave Flux</a> 30 min
  <br> 
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDSLF</td> <td>[LSA-204]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MDSLF</td> <td>[DEMO]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>

  <tr> <td>MDIDSLF</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/9BQa6e2CAaJdjRZ" target="_blank">Daily Downward Surface Longwave Flux</a>
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDIDSLF</td> <td>[LSA-206]</td> <td>2016-NRT</td> </tr>
  <tr> <td>MDIDSLF</td> <td>[DEMO]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MDIDSSF</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/QSABgnG4dZGBo5W" target="_blank">Daily Downward Surface Shortwave Flux</a>
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MDIDSSF</td> <td>[LSA-203]</td> <td>2004-NRT</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MNSLF</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/z42FQpGPmTxMN6Q" target="_blank">Daily Net Surface Longwave</a>
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MNSLF</td> <td>[LSA-208]</td> <td>2020-NRT</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  

  <tr> <td colspan="4" style="text-align: center"><b>
  <a href="https://landsaf.ipma.pt/en/data/products/evapotranspiration-turbulent-fluxes/" target="_blank">Evaporation and turbulent fluxes</a></b></td> </tr> <tr> 
  
  <tr> <td>METREF</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/zzBDmfgtJE9ePQW" target="_blank">Reference Evapotranspiration</a> [daily]
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>METREF</td> <td>[LSA-303]</td> <td>2016-NRT</td> </tr>
  <tr> <td>METREF-R</td> <td>[DEMO]</td> <td>2004-2015</td> </tr>
  </table>
  </td> <td>MSG, MSG-IODC</td> <td>HDF5, NETCDF</td> </tr>

  <tr> <td>MDMETv3</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/7QLcZfABg5H6mkq" target="_blank">Daily Evapotranspiration version 3</a>
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>DMETv3</td> <td>[LSA-312.3]</td> <td>2021-NRT</td> </tr>
  <tr> <td>DMETv3-R</td> <td>[LSA-351]</td> <td>2004-2020</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>

  <tr> <td>METv3</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/7QLcZfABg5H6mkq" target="_blank">Evapotranspiration version 3</a> [30 min]
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>METv3</td> <td>[LSA-311.3]</td> <td>2021-NRT</td> </tr>
  <tr> <td>METv3-R</td> <td>[LSA-350]</td> <td>2004-2020</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MHv3</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/7QLcZfABg5H6mkq" target="_blank">Sensible heat flux version 3</a> [30 min]
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MHv3</td> <td>[LSA-304.3]</td> <td>2021-NRT</td> </tr>
  <tr> <td>MHv3-R</td> <td>[LSA-352]</td> <td>2004-2020</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MLEv3</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/7QLcZfABg5H6mkq" target="_blank">Latent heat flux version 3</a> [30 min]
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MLEv3</td> <td>[LSA-305.3]</td> <td>2021-NRT</td> </tr>
  <tr> <td>MLEv3-R</td> <td>[LSA-353]</td> <td>2004-2020</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>

  
  <tr> <td>MDMET</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/xtAx57TM9qn5X4x" target="_blank">Daily Evapotranspiration</a>
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>DMETv3</td> <td>[LSA-312]</td> <td>2015-NRT</td> </tr>
  </table> 
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MET</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/GYmE6w75fPtQwrz" target="_blank">Evapotranspiration</a> [30 min]
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MET</td> <td>[LSA-311]</td> <td>2019-NRT</td> </tr>
  </table>
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  
  <tr> <td>MH</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/GYmE6w75fPtQwrz" target="_blank">Sensible heat flux</a> [30 min]
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MH</td> <td>[LSA-304]</td> <td>2019-NRT</td> </tr>
  </table> 
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  

  <tr> <td>MLE</td> <td>
  <a href="https://nextcloud.lsasvcs.ipma.pt/s/GYmE6w75fPtQwrz" target="_blank">Latent heat flux</a>[30 min]
  <br>
  <table>
  <tr> <td style="text-align: center" colspan="3"> MSG products info </td> </tr>
  <tr> <td>MLE</td> <td>[LSA-305]</td> <td>2019-NRT</td> </tr>
  </table>   
  </td> <td>MSG</td> <td>HDF5, NETCDF</td> </tr>
  

  <tr> <td colspan="4" style="text-align: center"><b>
  <a href="https://hsaf.meteoam.it/" target="_blank">H SAF Products</a></b></td> </tr> <tr> 

  <tr> <td>MDSC</td> <td>
  Daily snow cover (<a href="https://hsaf.meteoam.it/Products/Detail?prod=H31" target="_blank">H SAF H31</a>)</td> <td>MSG</td> <td>HDF5</td> </tr>

  <tr> <td>EDSC</td> <td>
  Daily Snow Cover (<a href="https://hsaf.meteoam.it/Products/Detail?prod=H32" target="_blank">H SAF H32</a>)</td> <td>EPS</td> <td>HDF5</td> </tr>  
 
</table>

**Disclaimer**:<br> All intellectual property rights of the LSA SAF products belong to EUMETSAT. The use of these products is granted to every interested user, free of charge. If you wish to use these products, EUMETSAT's copyright credit must be shown by displaying the words "copyright (year) EUMETSAT" on each of the products used.


