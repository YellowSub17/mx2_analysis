

import h5py
import hdf5plugin
import sys
import numpy as np


import matplotlib.pyplot as plt




h5file = h5py.File('/media/pat/datadrive/mx2tape/lyso_control1_run87/lyso_control1_0087_data_000170.h5', 'r')
d_shape = h5file['/entry/data/data'][:].shape
h5file.close()


h5file = h5py.File('/media/pat/datadrive/mx2tape/mask.h5', 'r')
mask = h5file['/entry/data/data'][:]
h5file.close()




run_mean = np.zeros(mask.shape)
run_std = np.zeros(mask.shape)


h5file = h5py.File('/media/pat/datadrive/mx2tape/lyso_control1_run87/lyso_control1_0087_data_000170.h5', 'r')


for i in range(d_shape[0]):
    print(i)
    run_mean += h5file['/entry/data/data'][i,:,:]
    run_std +=  h5file['/entry/data/data'][i,:,:]**2





h5file.close()

run_mean *= 1/d_shape[0]
run_mean *= mask

run_std *= 1/d_shape[0]
run_std *= mask

run_std = np.sqrt(run_std - run_mean**2)



# loc = np.where(run_mean>20)
loc = np.where(np.isnan(run_std))






plt.figure()
plt.imshow(run_mean)

plt.figure()
plt.imshow(run_std)


# loc = np.where( masked_d > np.max(masked_d)*0.9 )

mask[loc]=0



h5file = h5py.File('/media/pat/datadrive/mx2tape/mask.h5', 'w')
h5file['/entry/data/data'] = mask
h5file.close()






plt.show()
