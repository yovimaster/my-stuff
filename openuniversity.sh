#!/bin/bash

URL=$1
BASENAME='media_b1800000'
token=(${URL//\?/ })
VAR=(${URL//\// })

VIDEOPATH='https://souvod.bynetcdn.com/vod/smil:vod/openu/'${VAR[5]}'/'${VAR[6]}'/App/'${VAR[6]}'_10.smil'

for i in {1..1200}
do
FILENAME=$BASENAME'_'$i'.ts?'${token[1]}
FULLPATH=$VIDEOPATH/$FILENAME
wget $FULLPATH
cat $FILENAME >> $2'.mp4'
rm $FILENAME
done
