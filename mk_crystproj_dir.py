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
shutil.copy('./mx2eiger.geom', f'{CRYSTFELDIR}/{RUNID}/mx2eiger.geom93l.pdb')






glob_term = f'{DATADIR}/*_{RUNID}_data*'
lst_files = glob.glob(glob_term)

print(f'##Found {len(lst_files)} data h5s in {glob_term}')




for lst_file in lst_files:
    print(f'#writing {lst_file} to {RUNID}files.lst')
    for frame_num in range(200):
        lst_line = f'{h5file} //{frame_num}'
        cmd = f'echo {lst_line} >> {CRYSTFELDIR}/{RUNID}/{RUNID}files.lst'
        os.system(cmd)























