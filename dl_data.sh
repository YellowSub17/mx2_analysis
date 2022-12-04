#!/bin/bash


EMAIL='s3826109@student.rmit.edu.au'

DATADIR='/data/mx/1975a'

echo rsync -rtzP $EMAIL@sftp.synchrotron.org.au:$DATADIR .
