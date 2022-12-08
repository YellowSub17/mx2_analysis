#!/usr/bin/env python3


import os

import glob

import sys
import shutil



#dir where data is saved
DATADIR= '/beegfs/desy/user/patricka/mx2/data'

#dir to save crystfel project
CRYSTFELDIR= '/beegfs/desy/user/patricka/mx2/crystfel_calc'


RUNID = sys.argv[1]


#make dir to save data
if not os.path.exists(f'{CRYSTFELDIR}/{RUNID}'):
    os.mkdir(f'{CRYSTFELDIR}/{RUNID}')


shutil.copy('./crystfel.project.default', f'{CRYSTFELDIR}/{RUNID}/crystfel.project')
shutil.copy('./193l.pdb', f'{CRYSTFELDIR}/{RUNID}/193l.pdb')






glob_term = f'{DATADIR}/*_{RUNID}_data*'
lst_files = glob.glob(glob_term)

print(f'##Found {len(lst_files)} data h5s using term {glob_term}')




# for h5file in h5files:
    # for frame_num in range(200):
        # lst_line = f'{h5file} //{frame_num}'
        # cmd = f'echo {lst_line} >> {CRYSTFELDIR}/{RUNID}/run{RUNID}files.lst'
        # os.system(cmd)























