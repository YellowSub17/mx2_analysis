#!/usr/bin/env python3


import os

import glob

import sys




DATADIR= '/beegfs/desy/user/patricka/mx2/data'
CRYSTFELDIR= '/beegfs/desy/user/patricka/mx2/crystfel_calc'


RUNID = sys.argv[1]



h5files = glob.glob(f'{DATADIR}/*_{RUNID}_data*')

os.mkdir(f'{CRYSTFELDIR}/{RUNID}')

for h5file in h5files:
    for frame_num in range(200):
        print(f'{h5file} //{frame_num}')




















