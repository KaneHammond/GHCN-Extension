import os
import pandas as pd
import sys
from ftplib import FTP
import csv
import io

# This section will return multiple FIPS from list of state names.

# local_full_path = 'Retrieve_Files/States.csv.txt'

# FIPS = []

# def get_station_id():
# 	print('Enter station name, full or partial:')
# 	a = [str(x) for x in raw_input().upper().split(', ')]
# 	print('')
# 	dfM = pd.read_csv('Retrieve_Files/States.csv')
# 	dfM['STATE_NAME'] = dfM['STATE_NAME'].str.upper()
# 	# dfM.index.name = 'Index'
# 	print('Searching records...')
# 	for aItem in a:
# 		try:
# 			matches = dfM['STATE_NAME'].str.contains(aItem)
# 			df = dfM.loc[matches, ['STATE', 'STUSAB', 'STATE_NAME', 'STATENS']]
# 			matches = dfM
# 			# print df
# 			# FIPS.append(df['STATE'])
# 			FIPS.append(df.iloc[0]['STATE'])
# 			print FIPS
# 		except:
# 			print('Station not found')
# 			sys.exit()
# get_station_id()
# print FIPS

#****************************************************************************

# Will prompt option to correct for spelling error FOR ONE STATE IN QUERY
# Does not accept list of states.
# local_full_path = 'Retrieve_Files/States.csv.txt'

# FIPS = []

# def get_station_id():
# 	print('Enter station name, full or partial:')
# 	a = [str(x) for x in raw_input().upper().split(', ')]
# 	print('')
# 	dfM = pd.read_csv('Retrieve_Files/States.csv')
# 	dfM['STATE_NAME'] = dfM['STATE_NAME'].str.upper()
# 	# dfM.index.name = 'Index'
# 	print('Searching records...')
# 	# for aItem in a:
# 	try:
# 		matches = dfM['STATE_NAME'].str.contains(a)
# 		df = dfM.loc[matches, ['STATE', 'STUSAB', 'STATE_NAME', 'STATENS']]
# 		matches = dfM
# 		# print df
# 		# FIPS.append(df['STATE'])
# 		FIPS.append(df.iloc[0]['STATE'])
# 		# print FIPS
# 	except:
# 		print('Station not found: %s' % (a))
# 		# sys.exit()
# 	selection = 'Index'						
# 	FIP = 'STATE'
# 	ST = 'STUSAB'
# 	STATE = 'STATE_NAME               '
# 	STATENS = 'STATENS'	
# 	print('{: <6}{: <6}{: <6}{: <31}{: >8}'.format(selection,FIP,ST,STATE,STATENS))
# 	print('-'*5 + ' ' + '-'*5 + ' ' + '-'*30 + ' ' + '-'*7)
# 	for i in list(dfM.index):
# 	    print('{: 4}: {: <6}{: <6}{: <31}{: >8}'.format(i,
#                                                           dfM.loc[i,'STATE'],
#                                                           dfM.loc[i,'STUSAB'],
#                                                           dfM.loc[i,'STATE_NAME'],
#                                                           dfM.loc[i,'STATENS']))
# 	try:
# 	    query = input('Enter selection (ex. 001, 42): ')
# 	    query = int(query)
# 	except:
# 	    print('Please enter valid selection (ex. 001, 42)')
# 	    sys.exit()
# 	FIPS.append(dfM.iloc[query]['STATE'])
	
# get_station_id()
# print FIPS

#****************************************************************************

# Working loop function for FIPS codes base off of custom csv.


# local_full_path = 'Retrieve_Files/States.csv.txt'

# FIPS = []

# def get_station_id():
# 	print('Enter state name(s):')
# 	a = [str(x) for x in raw_input().upper().split(', ')]
# 	print('')
# 	dfM = pd.read_csv('Retrieve_Files/States.csv')
# 	dfM['STATE_NAME'] = dfM['STATE_NAME'].str.upper()
# 	# dfM.index.name = 'Index'
# 	print('Searching records...')
# 	i=0
# 	for aItem in a:
# 		try:
# 			matches = dfM['STATE_NAME'].str.contains(aItem)
# 			df = dfM.loc[matches, ['STATE', 'STUSAB', 'STATE_NAME', 'STATENS']]
# 			matches = dfM
# 			# print df
# 			# FIPS.append(df['STATE'])
# 			FIPS.append(df.iloc[0]['STATE'])
# 			# print FIPS
# 		except:
# 			print('State not found: %s' % (aItem))
# 			selection = 'Index'						
# 			FIP = 'STATE'
# 			ST = 'STUSAB '
# 			STATE = 'STATE_NAME        '
# 			STATENS = 'STATENS'	
# 			print('{: <6}{: <6}{: <6}{: <31}{: >8}'.format(selection,FIP,ST,STATE,STATENS))
# 			print('-'*5 + ' ' + '-'*5 + ' ' + '-'*38 + ' ' + '-'*7)
# 			for i in list(dfM.index):
# 			    print('{: 4}: {: <6}{: <6}{: <31}{: >8}'.format(i,
# 		                                                          dfM.loc[i,'STATE'],
# 		                                                          dfM.loc[i,'STUSAB'],
# 		                                                          dfM.loc[i,'STATE_NAME'],
# 		                                                          dfM.loc[i,'STATENS']))
# 			try:
# 			    query = input('Enter Index selection (ex. 001, 42): ')
# 			    query = int(query)
# 			except:
# 			    print('Please enter valid selection (ex. 001, 42)')
# 			    sys.exit()
# 			FIPS.append(dfM.iloc[query]['STATE'])
# 		i = i+1
# get_station_id()


#****************************************************************************

# Check Station Parameters
# Variable   Columns   Type
# ------------------------------
# ID            1-11   Character
# LATITUDE     13-20   Real
# LONGITUDE    22-30   Real
# ELEMENT      32-35   Character
# FIRSTYEAR    37-40   Integer
# LASTYEAR     42-45   Integer

output_dir = os.path.relpath('output')
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
ftp_path_dly_all = '/pub/data/ghcn/daily/'
local_full_path = 'output/ghcnd-inventory.txt'

def connect_to_ftp():
    """
    Get FTP server and file details
    """
    ftp_path_root = 'ftp.ncdc.noaa.gov'
    # Access NOAA FTP server
    ftp = FTP(ftp_path_root)
    message = ftp.login()  # No credentials needed
    # print(message)
    return ftp
def create_dataframe(element, dict_element):
    """
    Make dataframes out of the dicts, make the indices date strings (YYYY-MM-DD)
    """
    # element = element.upper()
    df_element = pd.DataFrame(dict_element)
    # print df_element

    # Separate dfs' pass this point containing data for full record.
    # Need to filter out unwanted data to ensure final output is complete.

    # Add dates (YYYY-MM-DD) as index on df. Pad days with zeros to two places
    df_element.index = df_element['YEAR'] + '-' + df_element['MONTH'] + '-' + df_element['DAY'].str.zfill(2)
    df_element.index.name = 'DATE'
    # Arrange columns so ID, YEAR, MONTH, DAY are at front. Leaving them in for plotting later - https://stackoverflow.com/a/31396042
    for col in ['DAY', 'MONTH', 'YEAR', 'ID']:
        df_element = move_col_to_front(col, df_element)
    # Convert numerical values to float
    df_element.loc[:,element] = df_element.loc[:,element].astype(float)
    # print df_element
    return df_element
    
def move_col_to_front(element, df):
    element = element.upper()
    cols = df.columns.tolist()
    cols.insert(0, cols.pop(cols.index(element)))
    df = df.reindex(columns=cols)
    return df

def dly_to_csv(ftp, station_id):    
	ftp_filename = 'ghcnd-inventory.txt'

	# Write .dly file to stream using StringIO using FTP command 'RETR'
	s = io.BytesIO()
	ftp.retrlines('RETR ' + ftp_path_dly_all + ftp_filename, s.write)
	s.seek(0)
	# print s
	# Write .dly file to dir to preserve original # FIXME make optional?
	with open(os.path.join(output_dir, ftp_filename), 'wb+') as f:
	    ftp.retrbinary('RETR ' + ftp_path_dly_all + ftp_filename, f.write)
	# print f
	# Move to first char in file
	s.seek(0)
	# File params
	num_chars_line = 269
	num_chars_metadata = 21
# Variable   Columns   Type
# ------------------------------
# ID            1-11   Character
# LATITUDE     13-20   Real
# LONGITUDE    22-30   Real
# ELEMENT      32-35   Character
# FIRSTYEAR    37-40   Integer
# LASTYEAR     42-45   Integer
	element_list = ['PRCP', 'SNOW', 'SNWD', 'TMAX', 'TMIN']
	dtype = {'STATION_ID': str,
			'LATITUDE': str,
			'LONGITUDE': str,
			'ELEMENT': str,
			'FIRSTYEAR': str,
			'LASTYEAR': str}
	names = ['STATION_ID', 'LATITUDE', 'LONGITUDE', 'ELEMENT', 'FIRSTYEAR', 'LASTYEAR']
	widths = [11,  # Station ID
				9,   # Latitude (decimal degrees)
				10,  # Longitude (decimal degrees)
				5,   # Element
				5,   # FY
				5]   # LY
	df = pd.read_fwf(local_full_path, widths=widths, names=names, dtype=dtype, header=None)
	print list(df.columns.values)
	print df
	

inFile = open('Retrieve_Files/output/Stations.csv', 'r')
theCsvData = csv.reader(inFile) #this creates a special object that the csv library knows how to access
allData=[]

#This takes the information read from the cvs and creates an index from it
for aRow in theCsvData:
  allData.append(aRow[:])

# Write list for station ids
stations = []
# Split dataset id and station id, keep station id ([-1])
for aRow in allData:
    temp = str(aRow[-4])
    new = temp.split(':', 1)[-1]
    stations.append(new)


for aRow in stations:
    station_id=aRow
    print station_id
    ftp = connect_to_ftp()
    dly_to_csv(ftp, station_id)
    ftp.quit()

#****************************************************************************
