
import os
import pandas as pd
import sys
from ftplib import FTP
import csv
import io


output_dir = os.path.relpath('output')
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
ftp_path_dly_all = '/pub/data/ghcn/daily/'
local_full_path = 'output/ghcnd-inventory.txt'

#************************************ DATA COVERAGE CHECK FTP
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

def Inventory(ftp):    
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
# ftp = connect_to_ftp()
# Inventory(ftp)

# ******************************* NATION LIST/CODES FTP

ftp_path_dly_all = '/pub/data/ghcn/daily/'
local_full_path = 'output/ghcnd-countries.txt'

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

def countries(ftp):    
    ftp_filename = 'ghcnd-countries.txt'

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
    print list(df.columns.values)
    print df

# ftp = connect_to_ftp()
# countries(ftp)

# ******************************* STATE/PROVINCE CODES (US AND CANADA) FTP

ftp_path_dly_all = '/pub/data/ghcn/daily/'
local_full_path = 'output/ghcnd-states.txt'

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

def State_Province_Codes(ftp):    
    ftp_filename = 'ghcnd-states.txt'

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

# ------------------------------
# Variable   Columns   Type
# ------------------------------
# CODE          1-2    Character
# NAME         4-50    Character
# ------------------------------
    dtype = {'CODE': str,
            'STATE': str}
    names = ['CODE', 'STATE']
    widths = [2,  # CODE
                47]   # COUNTRY
    df = pd.read_fwf(local_full_path, widths=widths, names=names, dtype=dtype, header=None)
    print list(df.columns.values)
    print df

# ftp = connect_to_ftp()
# State_Province_Codes(ftp)

# *************************************************STATION IDS

ftp_path_dly_all = '/pub/data/ghcn/daily/'
local_full_path = 'output/ghcnd-stations.txt'

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

def StationIDs(ftp):    
    ftp_filename = 'ghcnd-stations.txt'

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

# ------------------------------
# Variable   Columns   Type
# ------------------------------
# ID            1-11   Character (FIRST 2 CHAR IS COUNTRY)
# LATITUDE     13-20   Real
# LONGITUDE    22-30   Real
# ELEVATION    32-37   Real
# STATE        39-40   Character (ONLY US)
# NAME         42-71   Character
# GSN FLAG     73-75   Character
# HCN/CRN FLAG 77-79   Character
# WMO ID       81-85   Character
# ------------------------------
    dtype = {'COUNTRY': str,
             'STATION_ID': str,
             'LATITUDE': str,
             'LONGITUDE': str,
             'ELEVATION': str,
             'STATE': str,
             'STATION_NAME': str,
             'GSN_FLAG': str,
             'HCN_CRN_FLAG': str,
             'WMO_ID': str}
    names = ['COUNTRY','STATION_ID', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'STATE', 'STATION_NAME', 'GSN_FLAG', 'HCN_CRN_FLAG', 'WMO_ID']
    widths = [2,    # Country
              9,  # Station ID
              9,   # Latitude (decimal degrees)
              10,  # Longitude (decimal degrees)
              7,   # Elevation (meters)
              3,   # State (USA stations only)
              31,  # Station Name
              4,   # GSN Flag
              4,   # HCN/CRN Flag
              6]   # WMO ID
    df = pd.read_fwf(local_full_path, widths=widths, names=names, dtype=dtype, header=None)
    print list(df.columns.values)
    print df

ftp = connect_to_ftp()
StationIDs(ftp)