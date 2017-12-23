#!/bin/bash

BASENAME='media_b1200000'
VIDEOPATH='https://sslstream.bynetcdn.com/vod/mp4:vod/openu/PRV/ugBREejW2e/App/ugBREejW2e_2.mp4'


for i in {1..1000}
do
FILENAME=$BASENAME'_'$i'.ts'
FULLPATH=$VIDEOPATH/$FILENAME
wget $FULLPATH
cat $FILENAME >> 'fullvideo.ts'
rm $FILENAME
done
