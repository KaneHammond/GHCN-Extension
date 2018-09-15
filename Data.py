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