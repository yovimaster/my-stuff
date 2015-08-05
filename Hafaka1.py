# coding: utf-8
__author__    = 'Yoav T L'

import os	
import sys
import zipfile
import time
import boto
import datetime

today = str((time.strftime("%d/%m/%Y"))).replace('/','') #fetch the date
finalfile = "hafaka%s.zip"%today 
myZipFile = zipfile.ZipFile(finalfile, "w" ) #the zip file to upload
logfile = open('log.txt','a') #log file to write when was the last change
logtime = os.path.getmtime('.\log.txt') #get the time of the last log file 
logtimenotunix = datetime.datetime.fromtimestamp(int(logtime)).strftime('%Y-%m-%d %H:%M:%S')
logfile.write('The last hafaka was done on: %s \n ---------------------------------------------------------------------------------------------------------------------------------- \n '%logtimenotunix)
pat = ".\ravmilim_mdl"
for root, dirs, files in os.walk(pat): #takes all the files that were created after the last log file was created
    for i in files:
		g = os.path.join(pat,i)
		l = os.path.getmtime(g)
		if l > logtime and i != 'RAVMILIM.ZIP':
				print i
				myZipFile.write(g)

                
myZipFile.close()
logfile.close()
"""

# AWS ACCESS DETAILS
AWS_ACCESS_KEY_ID = '???'
AWS_SECRET_ACCESS_KEY = '???'

#AWS connect
from boto.s3.connection import S3Connection
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucketobj = conn.get_bucket('uploadir')

print 'Uploading file to Amazon S3'
 
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

from boto.s3.key import Key
k = Key(bucketobj)
k.key = '%s'%finalfile
k.set_contents_from_filename(finalfile, cb=percent_cb, num_cb=10)
"""
