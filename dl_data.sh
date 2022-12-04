#!/bin/bash


EMAIL='s3826109@student.rmit.edu.au'




DATADIR='/data/mx/19754a/frames/riboldia/d'

SAVEDIR='/media/pat/datadrive/mx2tape/lyso_jinxed_run92/'


#rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR/lyso_control1_0087_data_000170.h5 $SAVEDIR
#rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR/lyso_control1_0087_master.h5 $SAVEDIR
rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR/lyso_jinxed_alessa_1_0092_data_000001.h5 $SAVEDIR

