from ftplib import FTP

host = r'ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/hcn/'

#for example
# ftp.login("anonymous", "ftplib-example-1")
# data = []
# ftp.dir(data.append)
# ftp.quit()
# for line in data:
#     print line

import urllib 

Doc = urllib.urlretrieve(host, 'USW00023183.dly')
