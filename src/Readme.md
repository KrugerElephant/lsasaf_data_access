This folder contains several example to access LSA SAF products via OpenDAP in the thredds server

**Notes**

(May 2023) To run in google colab:
- Clone the repository to local env. to access the module thredds_lsasaf_utils.py  
- install the netCDF4 python library, but a version prior to 1.6 ([see](https://github.com/Unidata/netcdf4-python/issues/1179))  
- Add the following Cell to the start to the notebook:

```python
#Clone the repository to local env. to access the module thredds_lsasaf_utils.py
!rm -rf /content/lsasaf_data_access/
!git clone https://gitlab.com/helpdesk.landsaf/lsasaf_data_access.git
import sys
sys.path.insert(0,'/content/lsasaf_data_access/examples/thredds/')
# Required to load netcdf files using OpenDAP (valid in May 2023)
!pip install "netcdf4<1.6"
```


