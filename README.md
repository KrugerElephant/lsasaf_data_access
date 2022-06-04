# lsasaf_data_access

Useful information to access the LSA SAF Data Service

https://datalsasaf.lsasvcs.ipma.pt/

## Support
Check our webpage for an overview of the available data https://landsaf.ipma.pt/en/

Contact us via helpdesk.landsaf@ipma.pt 

## Usage
In addition to the direct download of the products via the web browser, the recomended way to download several products is with the [**wget**](https://www.gnu.org/software/wget/ 
) tool which is available in most linux distributions. For windows details will be included


For example to download MSG LST hourly files (skipping minutes 15, 30, 45) for Jan 2006 you can use the following command (don’t forget the last “/” to download only that period) (replace --user=XXX --password=XXX by your access credentials):
```
wget -c --no-check-certificate -r -np -nH \
     --user=XXX --password=XXX \
     -R "*15.nc, *30.nc, *45.nc, *.html" \
     https://datalsasaf.lsasvcs.ipma.pt/PRODUCTS/MSG/MLST/NETCDF/2006/01/
```
You can check the details of each option [here](https://www.gnu.org/software/wget/manual/wget.html). If you add the option “-nd” all files are saved to the current directly, otherwise they will be downloaded to a folder structure PRODUCTS/MSG/MLST/NETCDF/2006/01/

Check other examples in the repository: (to be included)

## Contributing
Contributions with examples accessing the data service (tools, scripts, etc...) are welcome

## License

Copyright (c) 2022 LSA SAF (https://landsaf.ipma.pt/en/)

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

