from DataFetch import*


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

#********************************Identify {endpoint} for URL
#********************************Identify {endpoint} for URL

Endpoint = '/datasets'

#********************************Location ID
#********************************Location ID

#^Place at start of argument
#*Edit Station FIP
ID = '38035'

# Define Location variable (fixed, do not edit)
Location = '?locationid=FIPS:%s' % (ID)

#********************************Station ID
#********************************Station ID

#^Place at start of argument
#*Edit Station ID
SI = 'GHCND:USC00323117'

# Define station ID variable fixed, do not edit)
Station = '?stationid=%s' % (SI)

#********************************Data Type ID
#********************************Data Type ID

# Common Variables = PRCP SNOW SNWD TMAX TMIN TOBS
#*Edit Variables, all caps separate by &
VariablesDT = 'SNOW&PRCP&TMAX%TMIN%TOBS'

# Define data type (fixed, do not edit)
DataType = '&datatypeid='+VariablesDT

#********************************Time Variables
#********************************Time Variables

#*****Edit Variables
STime = '1950-01-01'
ETime = '2018-01-01'

# Define Start and End date (fixed, do not edit)
StartDate = '&startdate='+STime
EndDate = '&enddate='+ETime

#********************************Sort Order
#********************************Sort Order

#*Edit SO to change sort order. Variables: asc or desc. Defaults to asc
SO = 'desc'

# Define Sort Field variable (fixed, do not edit)
SortO = '&sortorder=%s' % (SO) 

#********************************LIMIT
#********************************LIMIT

#*Edit Variable
LV = 20

# Define limit (fixed do not edit)
Limit = '&limit=%i' % (LV)

#********************************Offset 
#********************************Offset 

#*Edit Variable to change offset
OV = 0

# Define offset (fixed do not edit)
Offset = '&offset=%i' % (OV)

#********************************Choose arguments to pass for selection
#********************************Choose arguments to pass for selection
####Library of arguments:####
	# Location: This is a FIPS identifier for the county of interest
	# Station: Specific station ID
	# DataType: Can choose specific type of weather, temperature, cloud cover, etc.
	# StartDate: Date for the beginning of data
	# EndDate: Date for end of the data
	# SortO: This is for sorting by listing order 
	# Limit: Sets the maximimum of allowable returned records
	# Offset: Define which record (by index) to begin with

# Argument must start with Location, Extent, or DataSetID due to format.

Arguments = Station+StartDate+EndDate+Limit+DataType

print Arguments

#********************************Define data pull
url = (url+Endpoint+Arguments)
print url
response = requests.get(url, headers=headers)
response = response.json()
print response