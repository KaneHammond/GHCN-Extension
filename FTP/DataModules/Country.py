
import os
import pandas as pd
import sys
from ftplib import FTP
import csv
import io
sys.path.append("output")


output_dir = os.path.relpath('output/Country')
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)

# Definition for printing full dataframe
def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')
#************************************ DATA COVERAGE CHECK FTP
ftp_path_dly = '/pub/data/ghcn/daily/'
ftp_path_dly_all = '/pub/data/ghcn/daily/all/'
local_full_path = 'output/Country/ghcnd-inventory.txt'

def connect_to_ftp():
    """
    Get FTP server and file details
    """
    ftp_path_root = 'ftp.ncdc.noaa.gov'
    # Access NOAA FTP server
    ftp = FTP(ftp_path_root)
    message = ftp.login()  # No credentials needed
    print(message)
    return ftp

def Inventory(ftp):    
    ftp_filename = 'ghcnd-inventory.txt'

    # Write .dly file to stream using StringIO using FTP command 'RETR'
    s = io.BytesIO()
    ftp.retrlines('RETR ' + ftp_path_dly + ftp_filename, s.write)
    s.seek(0)

    with open(os.path.join(output_dir, ftp_filename), 'wb+') as f:
        ftp.retrbinary('RETR ' + ftp_path_dly + ftp_filename, f.write)
    # print f
    # Move to first char in file
    s.seek(0)

    # Variable   Columns   Type
    # ------------------------------
    # ID            1-11   Character
    # LATITUDE     13-20   Real
    # LONGITUDE    22-30   Real
    # ELEMENT      32-35   Character
    # FIRSTYEAR    37-40   Integer
    # LASTYEAR     42-45   Integer
    dtype = {'STATION_ID': str,
    		'LATITUDE': str,
    		'LONGITUDE': str,
    		'ELEMENT': str,
    		'FIRSTYEAR': str,
    		'LASTYEAR': str,}
    names = ['STATION_ID', 'LATITUDE', 'LONGITUDE', 'ELEMENT', 'FIRSTYEAR', 'LASTYEAR']
    widths = [11,  # Station ID
    			9,   # Latitude (decimal degrees)
    			10,  # Longitude (decimal degrees)
    			5,   # Element
    			5,   # FY
    			5]   # LY
    df = pd.read_fwf(local_full_path, widths=widths, names=names, dtype=dtype, header=None)
    # Write country codes and insert into df
    CC = []
    for aItem in df['STATION_ID']:
        CC.append(aItem[0:2])
    df.insert(0, 'COUNTRY_CODE', value=CC)
    return df

# ftp = connect_to_ftp()
# Inventory(ftp)

# ******************************* NATION LIST/CODES FTP

ftp_path_dly = '/pub/data/ghcn/daily/'
ftp_filename = 'ghcnd-countries.txt'

def connect_to_ftp():
    """
    Get FTP server and file details
    """
    ftp_path_root = 'ftp.ncdc.noaa.gov'
    # Access NOAA FTP server
    ftp = FTP(ftp_path_root)
    message = ftp.login()  # No credentials needed
    print(message)
    return ftp

def countries(ftp):    
    ftp_full_path = os.path.join(ftp_path_dly, ftp_filename)
    local_full_path = os.path.join(output_dir, ftp_filename)
    if not os.path.isfile(ftp_filename):
        with open(local_full_path, 'wb+') as f:
            ftp.retrbinary('RETR ' + ftp_full_path, f.write)

# Variable   Columns   Type
# ------------------------------
# CODE          1-2    Character
# NAME         4-50    Character
# ------------------------------
    dtype = {'CODE': str,
            'COUNTRY': str}
    names = ['CODE', 'COUNTRY']
    widths = [2,  # CODE
                48]   # COUNTRY
    df = pd.read_fwf(local_full_path, widths=widths, names=names, dtype=dtype, header=None)
    print ('View List of Available Countries?\n 1.     Yes\n 2.      No')
    query = input('Enter selection (ex. 001, 1): ')
    query = int(query)
    if query==1:
        print_full(df)
    print('Enter County Code(s):')
    a = [str(x) for x in raw_input().upper().split(', ')]
    print('')
    # # print list(df.columns.values)
    # try:
    #     print ('View List of Available Countries?\n 1.     Yes\n 2.      No')
    #     query = input('Enter selection (ex. 001, 1): ')
    #     query = int(query)
    #     if query==1:
    #         print_full(df)
    #     print('Enter state name(s):')
    #     a = [str(x) for x in raw_input().upper().split(', ')]

    # except:
    #     print('Please enter valid selection (ex. 001, 42)')
    #     sys.exit()
    print('Searching records...')
    i=0
    for aItem in a:
        matches = df['CODE'].str.contains(aItem)
        dfM = df.loc[matches, ['CODE', 'COUNTRY']]
        matches = dfM
        try:
            if len(matches)==1:
                Countries.append(matches.iloc[0]['CODE'])
            if len(matches)>1:
                dfM.reset_index(drop=True, inplace=True)
                dfM.index = dfM.index+1
                CODE = str('CODE')
                COUNTRY = str('COUNTRY')
                print('{: <6}{: <31}'.format(CODE,COUNTRY))
                print('-'*5 + ' ' + '-'*15 + '-'*10)
                for i in list(dfM.index):
                    print('{: 4}: {: <14}{: <9}'.format(i,
                                                dfM.loc[i,'CODE'],
                                                dfM.loc[i,'COUNTRY'])) 
                print('Country not found: %s' % (aItem))
                print ('Select Correct Country')
                query = input()
                query = int(query)
                Countries.append(dfM.loc[query, 'CODE'])
        except:
            print ('Country Code %s Not Found' % (aItem))
            sys.exit()

Countries = []
ftp = connect_to_ftp()
countries(ftp)
print Countries
