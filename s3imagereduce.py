#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import boto3
import urllib
import sys
import datetime
from dateutil.tz import tzutc
from subprocess import call
import csv

client = boto3.Session(profile_name='saml')
attr = client.client('s3')
attr2 = client.resource('s3')
bucket = 'dep-screenshots-s3-bucket'

Compressedtime = datetime.datetime(2017, 9, 7, tzinfo=tzutc())

def getimages(conn,merchant):
    paginator =conn.get_paginator('list_objects')
    operation_parameters = {'Bucket': bucket,
                        'Prefix': '{0}/{0}/SKU/'.format(merchant)}
    page_iterator = paginator.paginate(**operation_parameters)
    for page in page_iterator:
        print " starting list"
        parseimages(page)
        print "done"

def parseimages(objects):
    # print objects
    for key, value in objects.iteritems():
         if key == 'Contents':
             images = value
    print "starting to download"
    Downloadimage(images)

def Downloadimage(images):
    for i in images:
        fsize = i.values()[-1:]
        prefix = i.values()[3]
        filedate = i.values()[0]
        print(prefix)
        print(filedate)
        fname = prefix.split('/')[3]
        url = 'https://s3-us-west-2.amazonaws.com/{}/{}'.format(bucket,prefix)
        if filedate > Compressedtime:
        # if int(fsize[0]) > 100000 and : # need to be changed to date
            print url
            urllib.urlretrieve(url ,fname)
            print "file {} retrived - {}KB".format(fname,fsize)
            resizeImage(fname)
            uploadImage(attr2,prefix)

def resizeImage(fname):
    call(["node", "min.js",fname])

def uploadImage(conn,image):
    filen = image.split('/')[3]
    data = open("output/{}".format(filen), 'rb')
    conn.Bucket(bucket).put_object(Key=image, Body=data, ACL='public-read')
    data.close()
    os.remove("output/{}".format(filen))
    os.remove(filen)


with open('merchants.csv','rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['\xef\xbb\xbfShop'])
        getimages(attr,row['\xef\xbb\xbfShop'])
