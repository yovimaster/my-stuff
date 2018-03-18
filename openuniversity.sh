#!/bin/bash

BASENAME='media_b1800000'
VAR='XnO8F9g91u'
VIDEOPATH='https://sslstream.bynetcdn.com/vod/mp4:vod/openu/PRV1/'$VAR'/App/'$VAR'_6.mp4'


for i in {1..1000}
do
FILENAME=$BASENAME'_'$i'.ts'
FULLPATH=$VIDEOPATH/$FILENAME
wget $FULLPATH
cat $FILENAME >> 'fullvideo.ts'
rm $FILENAME
done
