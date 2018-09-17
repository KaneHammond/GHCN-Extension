from DataFetch import*

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

#********************************Identify {endpoint} for URL
#********************************Identify {endpoint} for URL

Endpoint = '/data'

#*******************************Dataset ID
#*******************************Dataset ID

#^Place at start of argument. Base argument requires this.
#*Edit station id (first part of code only)
IDnum = 'GHCND'
# Note*** GHCND:USC00323117 (single station) only works in Data endpoint

#Define Dataset ID (fixed, do  not edit)
DataSetID = '?datasetid=%s' % (IDnum)

#********************************Location ID Number
#********************************Location ID Number

#*Edit Station FIP
ID = '38035'

# Define Location variable (fixed, do not edit)
Location = '&locationid=FIPS:%s' % (ID)

#********************************Station ID
#********************************Station ID

#*Edit Station ID
SI = 'GHCND:USC00323117'

# Define station ID variable fixed, do not edit)
Station = '&stationid=%s' % (SI)

#********************************Data Type ID
#********************************Data Type ID

# Common Variables = PRCP SNOW SNWD TMAX TMIN TOBS
#*Edit Variables, all caps separate by &
VariablesDT = 'SNOW&PRCP&TMAX%TMIN%TOBS'

# Define data type (fixed, do not edit)
DataType = '&datatypeid='+VariablesDT

#********************************Time Variables
#********************************Time Variables

# CANNOT EXCEED 1 YEAR
#*****Edit Variables
STime = '1950-01-01'
ETime = '1951-01-01'

# Define Start and End date (fixed, do not edit)
StartDate = '&startdate='+STime
EndDate = '&enddate='+ETime

#********************************Units
#********************************Units

#*****Edit Variables
UnitVariable = 'metric'

# Define unit variable (fixed, do not edit)
Unit = '&unit=%s' % (UnitVariable)

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

#********************************Metadata
#********************************Metadata

#*Edit Variable (True or False, true by default)
MetaArg = 'true'

# Define Metadata variable (fixed do not edit)
Metadata = '&includemetadata=%s' % (MetaArg)

#********************************Choose arguments to pass for selection
#********************************Choose arguments to pass for selection
####Library of arguments:####
	# DataSetID: Letter code before station codes.
	# Location: This is a FIPS identifier for the county of interest
	# Station: Specific station ID
	# DataType: Can choose specific type of weather, temperature, cloud cover, etc.
	# StartDate: Date for the beginning of data
	# EndDate: Date for end of the data
	# Unit: Pick which units the data returned is in.
	# SortO: This is for sorting by listing order 
	# Limit: Sets the maximimum of allowable returned records
	# Offset: Define which record (by index) to begin with
	# Metadata: True or false, include metadata calculations.

# Argument must start with Location, Extent, or DataSetID due to format.

Arguments = DataSetID+Station+StartDate+EndDate+Unit+Limit

# print Arguments

#********************************Define data pull

# url = (url+Endpoint+Arguments)
# response = requests.get(url, headers=headers)
# print response.status_code
# print response.text
# response = response.json()
# Results = response['results']

# print Results
FinalDate = datetime.datetime.strptime('7/31/2018', '%m/%d/%Y')

PRCP = []
TOBS = []
TMAX = []
TMIN = []
SNOW = []
temp = []
i = 0

while i<=10:
	if i==0:
		url = (url+Endpoint+Arguments)
		response = requests.get(url, headers=headers)
		response = response.json()	
		Results = response['results']
	for aRow in Results:
		if aRow['datatype']=='PRCP':
			print aRow
			temp.append(aRow['value'])
			temp.append(aRow['date'])
			PRCP.append(temp)
		if aRow['datatype']=='TOBS':
			temp.append(aRow['value'])
			temp.append(aRow['date'])
			TOBS.append(temp)			
		if aRow['datatype']=='SNOW':
			temp.append(aRow['value'])
			temp.append(aRow['date'])
			SNOW.append(temp)
		if aRow['datatype']=='TMAX':
			temp.append(aRow['value'])
			temp.append(aRow['date'])
			TMAX.append(temp)
		if aRow['datatype']=='TMIN':
			temp.append(aRow['value'])
			temp.append(aRow['date'])
			TMIN.append(temp)
		i = i+1
		temp = []

print i
print TMAX
print len(TMAX)
print len(SNOW)
print len(PRCP)
print len(TOBS)