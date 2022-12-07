#!/bin/bash


EMAIL='s3826109@student.rmit.edu.au'


DATADIR='/data/mx/19754a/frames/riboldia/d'
SAVEDIR='/beegfs/desy/user/patricka/mx2/data'

FILENAME='lyso_jinxed_alessa_1_0092_mas*'

echo dl_data.sh: downloading data


rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR/$FILENAME $SAVEDIR



