from ftplib import FTP

try:
    import itertools
except:
    import pip
    pip.main(['install','itertools'])
    import itertools

import io
import copy
import csv
# ftp_path_dly_all = 'ftp.ncdc.noaa.gov'

# def connect_to_ftp():
#     """
#     Get FTP server and file details
#     """
#     ftp_path_root = 'ftp.ncdc.noaa.gov'
#     # Access NOAA FTP server
#     ftp = FTP(ftp_path_root)
#     message = ftp.login()  # No credentials needed
#     print(message)
#     return ftp

ftp = FTP('ftp.ncdc.noaa.gov')
message = ftp.login()
# print message
# return ftp
ftp.cwd('/pub/data/ghcn/daily/all/')


def grabFile():
	FileName = 'USC00323117.csv'
	localfile = open(FileName, 'wb')
	# s = io.BytesIO()
	# ftp.retrbinary('RETR ' + 'USC00323117.dly', s.write, 1024)
	ftp.retrbinary('RETR ' + 'USC00323117.dly', localfile.write, 1024)
 	# File params

grabFile()

inFile = open('USC00323117.csv', mode='rU')
theCsvData = csv.reader(inFile)
allData = []

for aRow in theCsvData:
	allData.append(aRow)
inFile.close()

for aRow in allData:
	# print aRow
	temp = copy.deepcopy(aRow)
	# break
	temp = temp.replace(" ", "-")
	break
print temp
print allData[0]
# outfile = open('USC00323117_2.csv', mode='wb')
# csv_f = csv.reader(infile)
# writer = csv.writer(outfile)
# next(csv_f)  # skip headers
# row = next(csv_f)
#     # row looks like
#     # ['one', 'two', 'three four', 'five', ...]

# rewritten_row = itertools.chain.from_iterable(
#     [cell.split() for cell in row])  # or map(str.split, row)
#     # rewritten_row looks like
#     # ['one', 'two', 'three', 'four', 'five', ...]
# for aItem in rewritten_row:
# 	print aItem
# # writer.writerow(rewritten_row)




