# GHCN-Extension
Objectives:
  1) Filter Through Global Historical Climatology Network (GHCN) Data Using Python
  2) Identify locations of interest via data attributes:
  
      * Spatial attributes
    
      * Data Coverage (percentage of record coverage)
    
      * Elevations
    
      * Data Type
    
      * Start and End dates
    
      * Station IDs and FIPS
    
  3) Extract station data fitting defined arguments (Either through API or FTP) 
  
###### Requirements:
This program requires python 2.7.

*Download => https://www.python.org/download/releases/2.7/

*Adding Paths => https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/

###### Files:

DataFetch.py: Primary file for running other API modules.

  Datasets.py: Module of DataFetch.py, used for searching for specific data sets through API.
  
  Stations.py: Module of DataFetch.py, used for searching for stations through API.
  
  Data.py: Module of DataFetch.py, used for searching for data, via link provided by either Datasets.py or Stations.py.
  
FTP.py: Currently a solo file. Will be linked with DataFetch.py as a module once working. FTP server is desired over API, larger sets of data can be downloaded at once. The original API modules are useful for filtering stations available on the server.
  
  

