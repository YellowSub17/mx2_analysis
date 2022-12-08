#!/usr/bin/env python3


import os

import glob

import sys
import shutil
import h5py



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






glob_term = f'{DATADIR}/*_{RUNID}_data*.h5'
h5_data_files = glob.glob(glob_term)

print(f'##Found {len(h5_data_files)} data h5s in {glob_term}')



lst_file = open(f'{CRYSTFELDIR}/{RUNID}/{RUNID}files.lst', 'w')

for h5_data_file in h5_data_files:
    print(f'#writing {h5_data_file} to {RUNID}files.lst')

    with h5py.File(h5_data_file, 'r') as f:
        n_frames, _, _ = f['/entry/data/data'].shape

    for frame_num in range(200):
        lst_file.write(f'{h5_data_file} //{frame_num}\n')























