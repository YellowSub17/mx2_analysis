

import h5py
import hdf5plugin
import sys
import numpy as np


import matplotlib.pyplot as plt





h5file = h5py.File('/media/pat/datadrive/mx2tape/lyso_control1_run87/lyso_control1_0087_master.h5', 'r')
d = h5file['/entry/instrument/detector/detectorSpecific/pixel_mask'][:]

h5file.close()



d[np.where(d>0)] = 2**10

d[np.where(d==0)] = 1

d[np.where(d==2**10)] = 0







h5file = h5py.File('/media/pat/datadrive/mx2tape/mask.h5', 'w')

h5file['/entry/data/data'] = d

h5file.close()

# plt.figure()
# plt.imshow(d, origin='lower', aspect='auto',  )
# plt.show()

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



loc1 = np.where(run_mean>20)
loc2 = np.where(np.isnan(run_std))


mask[loc1]=0
mask[loc2]=0





# plt.figure()
# plt.imshow(run_mean)

# plt.figure()
# plt.imshow(run_std)






h5file = h5py.File('/media/pat/datadrive/mx2tape/mask.h5', 'w')
h5file['/entry/data/data'] = mask
h5file.close()






plt.show()











