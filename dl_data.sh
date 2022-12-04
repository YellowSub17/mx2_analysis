#!/bin/bash


EMAIL='s3826109@student.rmit.edu.au'

DATADIR='/data/mx/19754a/frames/'



USER='riboldia'
GROUP='test_crystal'
RUN='0008'

#rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR$USER/$GROUP/$GROUP_$RUN_data_000001.h5 .
#rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR$USER/$GROUP/$GROUP_$RUN_master.h5 .


rsync -rtzP $EMAIL@sftp.synchrotron.org.au:/data/mx/19754a/frames/calibration/test_crystal/testcrystal_0012*.h5 ./testrun12/

