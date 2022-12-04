#!/bin/bash


EMAIL='s3826109@student.rmit.edu.au'


DATADIR='/data/mx/19754a/frames/riboldia/d'
SAVEDIR='/media/pat/datadrive/mx2tape/h5s'



FILENAME='lyso_jinxed_alessa_1_0094_data_000002.h5'


echo dl_data.sh: downloading data


rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR/$FILENAME $SAVEDIR


python decomp.py $SAVEDIR/$FILENAME

