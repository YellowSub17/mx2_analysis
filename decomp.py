
import h5py
import hdf5plugin
import sys
import numpy as np
import matplotlib.pyplot as plt


fname = sys.argv[1]
if fname[-3:]=='.h5':
    fname = fname[:-3]



print('decomp.py: opening mask')
with h5py.File(f'/media/pat/datadrive/mx2tape/mask.h5', 'r') as h5file_mask:
    mask = h5file_mask['entry/data/data'][:]



print('decomp.py: opening data')
with h5py.File(f'{fname}.h5','r') as h5file_data:
    d = h5file_data['/entry/data/data'][:]




print('decomp.py: masking data')
for i, frame in enumerate(d):
    print(i, end='\r')
    d[i] = mask*frame




print('decomp.py: saving masked data')
with h5py.File(f'{fname}_decomp.h5','w') as h5file_decomp:
    h5file_decomp['entry/data/data'] = d



