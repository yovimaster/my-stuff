# coding: utf-8
__author__    = 'Yoav T L'

import time
import sys 
import zipfile
import os
import shutil
import datetime
import subprocess

#2nd part of automation, unzip the files from hafaka and copy them into the right folder
#2- zip and backup the current local folder - [V]
#3- iis stop
#1- unzip 
#4- copy the unzipped files into folders 
#5- iis start

today = str((time.strftime("%d/%m/%Y"))).replace('/','') #fetch the date
backupname = 'ravmilim_%s.zip'%today


#hafakafile = sys.argv[1]
backupfolder = 'C:\ravmilim_mdl_python'
"""
def unzipfile(hafaka):
    zfile = zipfile.ZipFile(hafaka)
    os.chdir('C:\\')
    zfile.extractall(os.getcwd())
    zfile.close()
    
"""
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

myZipFile = zipfile.ZipFile(backupname, "w", zipfile.ZIP_DEFLATED)
zipdir(backupfolder,myZipFile)
myZipFile.close()
"""
shutil.move(backupname, "c:\\backups\\")
subprocess.call("iisreset -stop", shell=True)
 
unzipfile(hafakafile)

subprocess.call("iisreset -start", shell=True)
"""
time.sleep(2)

