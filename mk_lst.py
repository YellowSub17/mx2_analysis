#!/usr/bin/env python3


import os

import glob

import sys




DATADIR= '/beegfs/desy/user/patricka/mx2/data'
CRYSTFELDIR= '/beegfs/desy/user/patricka/mx2/crystfel_calc'


RUNID = sys.argv[1]



h5files = glob.glob(f'{DATADIR}/*_{RUNID}_data*')

print(f'##Found {len(h5files)} h5')




for h5file in h5files:
    for frame_num in range(200):
        lst_line = f'{h5file} //{frame_num}'
        cmd = f'echo {lst_line} >> {CRYSTFELDIR}/{RUNID}/run{RUNID}files.lst'
        os.system(cmd)























