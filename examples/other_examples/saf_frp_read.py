import h5py, os, sys
import numpy as np
import argparse






def get_h5_extra_info(fh):
    res = dict()
    for k in fh.attrs:
        res[k] = fh.attrs[k]
    return res

def get_h5_dataset(f, dsname):
    ds = dsname in f
    if ds:
        ds = f[dsname]
        d = ds[:]
        missing = ds.attrs.get("MISSING_VALUE")
        if missing is not None:
            mask = (d == missing)
        scale = ds.attrs.get("SCALING_FACTOR")
        offset = ds.attrs.get("OFFSET")
        if (scale is not None) and (offset is not None):
            d = d/scale + offset
        if missing is not None:
            d[mask] = np.nan
        return d
    else:
        f.close()
        print 'can not find dataset: "%s" in hdf5 file'%(dsname)
        sys.exit(run_status['UNABLE_TO_PROCESS'])

def read_lsasaf_h5(inputfiles):
    data = {}
    print '-'*80
    for f in inputfiles:
        path, filename = os.path.split(f)
        info = filename.split('_')
        if info[4] == 'MSG-Disk':
            print 'full disk input with time %s and product %s'%(info[5], info[3])
            t = info[5]
            k = info[3]
            try:
                fh = h5py.File(f, "r")
            except:
                print 'not a valid hdf5 file: ', 
                sys.exit(run_status['INPUT_NOT_FOUND'])
            else:
                if k == 'FRP-PIXEL-ListProduct':
                    ds = ['LONGITUDE', 'LATITUDE', 'FRP', 'FRP_UNCERTAINTY', 'PIXEL_ATM_TRANS', 'ABS_LINE', 'ABS_PIXEL']
                elif k == 'FRP-PIXEL-QualityProduct':
                    ds = ['QUALITYFLAG']
                elif k == 'FTA-FRP':
                    ds = ['GFRP','LATITUDE','LONGITUDE']    
                elif k == 'LAT' or k == 'LON':
                    t='static'
                    ds = [k]
                else:
                    continue
                if t not in data:
                    data[t] = {}
                for d in ds:
                    data[t][d] = get_h5_dataset(fh, d)
                if 'info' not in data and k == 'FRP-PIXEL-ListProduct':
                    data['infos'] = get_h5_extra_info(fh)
                fh.close()
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="example script in python using h5py to access datasets and attributes")
    parser.add_argument('full_filename',type=str,help="this is the file you want to open and read")
    args = parser.parse_args()

    #check if the file passed as agument exists
    if (not os.path.isfile(args.full_filename)):
        print("problem: the file %s doesnt exist." % args.full_filename)
        sys.exit(1)
    try:
        #open the file in reading mode
        f = h5py.File(args.full_filename,'r')
    except:
        print("problem: %s is not a valid hdf5 file" % args.full_filename)
        sys.exit(1)


    curr_workdir = os.getcwd()
    filename = os.path.join(curr_workdir,args.full_filename)
    parsed_date = filename[-12:]
    print(filename)
    dt = read_lsasaf_h5([filename])
    print(dt)
    FRP=np.flipud(dt[parsed_date]['FRP'])
    print(FRP)
