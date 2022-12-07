

import h5py
import hdf5plugin
import sys
import numpy as np


import matplotlib.pyplot as plt


# DATAFILE = '/media/pat/datadrive/mx2tape/h5s/lyso_control1_0087_data_000170.h5'
# MASKFILE = '/home/pat/Documents/cloudstor/phd/python_projects/mx2_analysis/mask.h5'
DATAFILE = '/beegfs/desy/user/patricka/mx2/data/lyso_jinxed_alessa_1_0092_data_000001.h5'
MASKFILE = '/beegfs/desy/user/patricka/mx2/crystfel_calc/mask.h5'

h5file_data = h5py.File(DATAFILE, 'r')
NFRAMES, EIGER_NX, EIGER_NY = h5file_data['entry/data/data'].shape
h5file_data.close()

NFRAMES=10


run_sum = np.zeros( (EIGER_NX, EIGER_NY) )
run_sumsq = np.zeros((EIGER_NX, EIGER_NY))



h5file = h5py.File(DATAFILE, 'r')
for i in range(NFRAMES):
    print(i)
    run_sum += h5file['/entry/data/data'][i,:,:]
    run_sumsq +=  h5file['/entry/data/data'][i,:,:]**2



h5file.close()

run_mean = run_sum/NFRAMES
run_std = np.sqrt(run_sumsq/NFRAMES - run_mean**2)



loc1 = np.where(run_mean>20)
loc2 = np.where(np.isnan(run_std))


mask = np.zeros((EIGER_NX, EIGER_NY))

mask[loc1]=1
mask[loc2]=1








h5file = h5py.File(MASKFILE, 'w')
h5file['/entry/data/data'] = mask
h5file.close()

















