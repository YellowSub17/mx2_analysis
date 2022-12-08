#!/usr/bin/env python3


import os

import glob




DATADIR= '/beegfs/desy/user/patricka/mx2/data'
CRYSTFELFIR= '/beegfs/desy/user/patricka/mx2/crystfel_calc'
RUNIDS = ['0091', '0092', '0102', '0103', '0105']

RUNIDS = ['0105']




for RUNID in RUNIDS:
    x = glob.glob(f'{DATADIR}/*_{RUNID}_*')

for i in x:
    print(i)
    
















