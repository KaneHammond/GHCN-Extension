from DataFetch import*


# /stations				*A station is a any weather observing platform where data is recorded.
#		Parameters:
#			datasetid 	*Specify specific dataset (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			locationid	*Specify location via location id (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			datacategoryid *Category id separated by ampersands
#			datatypeid	*Specify data types (Accepts a valid data type id or a chain of data type ids separated by ampersands.)
#			extent		*Desired geographical extent for search. 
# 				See link below for description (extent): 
#					https://developers.google.com/maps/documentation/javascript/reference/coordinates#LatLngBoundsLiteral
#			startdate	*ISO formated date: (yyyy-mm-dd) can be used without enddate
#			enddate		*ISO formated date: (yyyy-mm-dd) can be used without startdate
#			sortfield	*Sort by name, mindate, maxdate, and datacoverage fields
#			sortorder	*Which order to sort by asc or desc (asc is default)
#			limit 		*Limit of return (default is 25)
#			offset		*Offset the result list, begin with offset record (defaul is 0)


#********************************Identify {endpoint} for URL
#********************************Identify {endpoint} for URL

Endpoint = '/stations'

#*******************************Dataset ID
#*******************************Dataset ID

#^Place at start of argument
#*Edit station id (first part of code only)
IDnum = 'GHCND'
# Note*** GHCND:USC00323117 (single station) only works in Data endpoint

#Define Dataset ID (fixed, do  not edit)
DataSetID = '?datasetid=%s' % (IDnum)

#********************************Location ID Number
#********************************Location ID Number

#^Place at start of argument
#*Edit Station FIP
ID = '38'

# Define Location variable (fixed, do not edit)
Location = '?locationid=FIPS:%s' % (ID)

#********************************Choose Extent Parameters
#********************************Choose Extent Parameters

#^Place at start of argument
#*Edit North South East West****
North = 47.899684
South = 46.665508
East = -98.735426
West = -101.735426
# Define Extent variable (fixed, do not edit)
Extent = '?extent=%f,%f,%f,%f' % (South, West, North, East)

#********************************Data Category ID
#********************************Data Category ID

# Common Variables = TEMP
#*Edit Variables, all caps separate by &
VariablesDC = 'TEMP'

# Define data categories variable (fixed, do not edit)
DataCat = '&datacategoryid='+VariablesDC

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

#********************************Sort Field
#********************************Sort Field

#*Edit SF to change sort field. Variables: name, mindate, maxdate, and datacoverage
SF = 'mindate'

# Define Sort Field variable (fixed, do not edit)
SortF = '&sortfield=%s' % (SF) 

#********************************Sort Order
#********************************Sort Order

#*Edit SO to change sort order. Variables: asc or desc. Defaults to asc
SO = 'desc'

# Define Sort Field variable (fixed, do not edit)
SortO = '&sortorder=%s' % (SO) 

#********************************LIMIT
#********************************LIMIT

#*Edit Variable
LV = 500

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
	# DataSetID: This is an ID located before the specific station code
	# Location: This is a FIPS identifier for the county of interest
	# Extent: Coordinates defining an area of interest
	# DataCat: Categories of interest, not specific weather type
	# DataType: More specific than DataCat, can choose specific type of weather, temperature, etc.
	# StartDate: Date for the beginning of data
	# EndDate: Date for end of the data
	# SortF: This is for sorting by specific fields
	# SortO: This is for sorting by listing order 
	# Limit: Sets the maximimum of allowable returned records
	# Offset: Define which record (by index) to begin with

# Argument must start with Location, Extent, or DataSetID due to format.

Arguments = Location+StartDate+Limit+DataType+Limit

print Arguments

#********************************Define data pull
url = (url+Endpoint+Arguments)
# print url
response = requests.get(url, headers=headers)
response = response.json()
json_list = response['results']

# Make csv with useable stations. Filters data by date further than request.
Stations = []
Record = []
# Index record for while loop and json_list
i = 0
CheckDate = 0
while i<len(json_list):
	temp = response['results'][i]['id']
	Record.append(temp)
	temp = response['results'][i]['name']
	Record.append(temp)
	temp = response['results'][i]['maxdate']
	var = copy.deepcopy(temp)
	var = datetime.datetime.strptime(temp, '%Y-%m-%d')
	if var<(datetime.datetime.strptime('2016-11-01', '%Y-%m-%d')):
		CheckDate = 1
	Record.append(temp)
	temp = response['results'][i]['mindate']
	var = copy.deepcopy(temp)
	var = datetime.datetime.strptime(temp, '%Y-%m-%d')
	if var>(datetime.datetime.strptime('1950-10-01', '%Y-%m-%d')):
		CheckDate = 1
	Record.append(temp)
	if CheckDate<1:
		Stations.append(Record)
	Record = []
	i = i+1
	CheckDate = 0

with open('Stations.csv', 'wb') as f:
    writer = csv.writer(f)
    for aItem in Stations:
        writer.writerow(aItem)

