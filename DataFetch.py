try:
	import requests
except:
	import pip
	pip.main(['install','requests'])
	import requests

#### Token

# In order to download data through the NCDC on python, a token code must
# be requested. The link is: https://www.ncdc.noaa.gov/cdo-web/token

token = 'pwchfVkDdfQBazXlZMFLVcedSVaEieea'
headers = {'token': token}
#### URL link and parameters

# *** https://www.ncdc.noaa.gov/cdo-web/api/v2/{endpoint} ***
url = "https://www.ncdc.noaa.gov/cdo-web/api/v2"
### Options for Endpoints
# /datasets 			*A dataset is the primary grouping for data at NCDC.
#	/{id}					*Used to find information about dataset with id of {id}
#		Parameters:
#			datatypeid	*Specify data types (Accepts a valid data type id or a chain of data type ids separated by ampersands.) 
#			locationid	*Specify location via location id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			stationid	*Specify station id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)
#
# /datacategories 		*A data category is a general type of data used to group similar data types.
#		Parameters:
#			datasetid 	*Specify specific dataset (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			locationid	*Specify location via location id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			stationid	*Specify station id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			sortfield	*Sort by name, mindate, maxdate, and datacoverage fields
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)
#
# /datatypes 			*A data type is a specific type of data that is often unique to a dataset.
#		Parameters:
#			datasetid 	*Specify specific dataset (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			locationid	*Specify location via location id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			stationid	*Specify station id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			datacategoryid *Category id separated by ampersands
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			sortfield	*Sort by name, mindate, maxdate, and datacoverage fields
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)
#
# /locationcategories	*A location category is a grouping of similar locations.
#		Parameters:
#			datasetid 	*Specify specific dataset (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			sortfield	*Sort by name, mindate, maxdate, and datacoverage fields
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)
#
# /locations 			*A location is a geopolitical entity.
#		Parameters:
#			datasetid 	*Specify specific dataset (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			locationcategoryid *Location id or chain of location category ids separatede by ampersands.
#			datacategoryid *Category id separated by ampersands
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			sortfield	*Sort by name, mindate, maxdate, and datacoverage fields
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)
#
# /stations				*A station is a any weather observing platform where data is recorded.
#		Parameters:
#			datasetid 	*Specify specific dataset (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			locationid	*Specify location via location id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			datacategoryid *Category id separated by ampersands
#			datatypeid	*Specify data types (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			extent		*Desired geographical extent for search. 
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			sortfield	*Sort by name, mindate, maxdate, and datacoverage fields
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)
#
# /data 				*A datum is an observed value along with any ancillary attributes at a specific place and time.
#		Parameters:
#			datasetid 	*Specify specific dataset (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			locationid	*Specify location via location id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			datatypeid	*Specify data types (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			stationid	*Station id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			units		* metric or standard
#			sortfield	*Sort by name, mindate, maxdate, and datacoverage fields
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)
#			includemetadata *Default true, used to improve response time by preventing the calculation result of metadata.


#### Pagination
# limit					*Limits the amount of results returned.
# offset				*Begin with specific record number.

# Station parameters */stations*
# import Stations
# Stations
# from Stations import*

# Datasets parameters */datasets*
# import Datasets
# Datasets
# from Datasets import*

# Data parameters */data*
import Data
Data
from Data import*