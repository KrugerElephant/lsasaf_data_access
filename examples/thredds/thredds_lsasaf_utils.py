# Contains several utility functions to access LSA SAF data products via the Thredds server

from netCDF4 import Dataset
import datetime as dt
import pandas as pd
import time
import xarray as xr

from tqdm import tqdm # only for the nice progress bar

def load_product_slots_domain(product,slot_list,NcvarsLoad,LatLonBox=None,LatLonPoint=None):
    """
    Function to load time series of a given product for a given domain"
    Inputs:
    
    Returns:
    
    """
    
    Box=False
    Point=False
    if LatLonBox is not None and LatLonPoint is None:
        # List with Lon/Lat slices to be used by xarray to cut domain
        Box=True
        if "MSG" in product.path or "MSG-IODC" in product.path:
            LatLonSlice = [ slice(LatLonBox[1],LatLonBox[0]), ## swapped for MSG
                            slice(LatLonBox[2],LatLonBox[3])] 
        else:
            LatLonSlice = [ slice(LatLonBox[0],LatLonBox[1]),
                            slice(LatLonBox[2],LatLonBox[3])] 
    
    if LatLonBox is None and LatLonPoint is not None:
        Point=True
    
    if not Box and not Point:
        print("Must provide LatLonBox or LatLonPoint")
        return None
    
    tstart=time.time()
    ds_tmp=[] # temporary list to store datasets before concatenation
    slots_miss=[] # list to store missing files
    pbar = tqdm(slot_list) # to have a nice progress bar 
    for slot in pbar:
        furl = product.full_url(product.file_url(slot))

        # try to open with xarray as dataset
        try:
            ds = xr.open_dataset(furl)
        except:
            slots_miss.append(slot)
            continue
        try:
            # cut domain and select variables 
            if Box:
                xtmp=ds.sel(lat=LatLonSlice[0],lon=LatLonSlice[1])[NcvarsLoad]
            elif Point:
                xtmp=ds.sel(lat=LatLonPoint[0],lon=LatLonPoint[1],method='nearest')[NcvarsLoad]
            xtmp.load() # force load of data at this stage 
            ds_tmp.append(xtmp)
        except:
            print("Some problem slicing the domain or getting the netcdf variable(s):",NcvarsLoad)
            print(f"Check: https://{product.server}/{product.file_url(slot)}.html")
            break
        pbar.set_description("Processing %s" % slot) # update progress bar 
    pbar.close()
    # We're done, now concatenate datasets in time dimension
    if len(ds_tmp) > 0 :
        ds_full=xr.concat(ds_tmp,dim='time')
        print(f"Loaded {len(slot_list)-len(slots_miss)} out of "
              f"{len(slot_list)} slots with dims: {ds_full.dims} "
              f"in {time.time()-tstart:.2f} seconds ")
        #display(ds_full)
        return ds_full
    else:
        print(f"Could not load any slot !")
        print(f"Check: https://thredds.lsasvcs.ipma.pt/thredds/")
        print(f"First: {product.file_url(slot_list[0])}")
        print(f"Last: {product.file_url(slot_list[-1])}")
        return None

def gen_slot_list(dstart,dend,product_freq):
    """
    Function to generate a list of slots
    """
    if product_freq == "day15":
        # special case for products on day 15
        dlist = [ dt.datetime(dd.year,dd.month,15) for dd in pd.date_range(dstart,dend,freq='M') ]
    else:
        dlist = pd.date_range(dstart,dend,freq=product_freq)

    return dlist 

class lsa_product:
    """
    Class to describe products
    Full file URL to be generated as:
    https://{user}:{passwd}@{server_url}/{product_path}/YYYY/MM/DD/{product_fname}_SLOT.nc
    """
    
    def __init__(self,product_path,product_fname,server_url="thredds.lsasvcs.ipma.pt/thredds/dodsC"):
        """
        Initialize product details:
        product_path: path of product in thredds server eg. /MSG/MTFVC/NETCDF/ p
        prouct_fname: file name of products, excluding slot, eg. NETCDF4_LSASAF_MSG_FVC-D10_MSG-Disk
        server_url: server URL
        """
        self.path=product_path
        self.fname=product_fname
        self.server=server_url
        self.user=None
        self.passwd=None
    
    def file_url(self,slot):
        """
        Function to generate and return file URL
        Inputs:
        slot: slot in datetime format
        Return:
        file_url: file URL
        """
        return f"{self.path}{slot.strftime('%Y/%m/%d/')}{self.fname}_{slot.strftime('%Y%m%d%H%M')}.nc"
        
        
    def full_url(self,file_url,check=False):
        
        """
        Function to generate and return full file URL
        Inputs:
        file url: slot in datetime format
        check: if True, tries to open the file
        Return:
        file_url: full file URL. 
                  If check is True and file can be opened, returns full file URL
                  If check is True and file cannot be opened, return None
        """
        full_url = f"https://{self.user}:{self.passwd}@{self.server}/{file_url}"
        
        if check:
            try:
                # try to open file 
                nc = Dataset(full_url,'r')
                nc.close()
            except:
                print("Could not open file:",file_url)
                full_url = None
        return full_url 
                    
