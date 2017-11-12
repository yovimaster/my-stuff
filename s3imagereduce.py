import os
import boto3
from PIL import Image
import urllib
import sys
import datetime
from dateutil.tz import tzutc


client = boto3.Session(profile_name='saml')
attr = client.client('s3')
attr2 = client.resource('s3')
bucket = 'dep-screenshots-s3-bucket'

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
    print " starting to download"
    Downloadimage(images)

def Downloadimage(images):
    for i in images:
        fsize = i.values()[-1:]
        prefix = i.values()[3]
        print(prefix)
        print(fsize)
        fname = prefix.split('/')[3]
        url = 'https://s3-us-west-2.amazonaws.com/{}/{}'.format(bucket,prefix)
        if int(fsize[0]) > 700000: # need to be changed to date
            print url
            urllib.urlretrieve(url ,fname)
            print "file {} retrived - {}KB".format(fname,fsize)
            resizeImage(fname)
            uploadImage(attr2,fname)

def resizeImage(fname):
    im = Image.open(fname)
    im.resize((int(float(im.size[0]*0.9)),(int(float(im.size[1]*0.9)))),Image.ANTIALIAS).save('small5.png',quality=15)
#
# def uploadImage(conn,image):
#     data = open(image, 'rb')
#     fullname='altrec/altrec/SKU/{}'.format(image)
#     conn.Bucket('yovi-test-images').put_object(Key=fullname, Body=data, ACL='public-read')

resizeImage('2017_06_15_12:12:02-S1j5KggX-.png')
# getimages(attr,'6pm')
