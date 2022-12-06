



import h5py
import hdf5plugin
import sys
import numpy as np


import matplotlib.pyplot as plt





# data_fname = '/media/pat/datadrive/mx2tape/h5s/lyso_jinxed_alessa_1_0092_data_000001_decomp.h5'
# mask_fname = '/media/pat/datadrive/mx2tape/mask.h5'



# with h5py.File(f'{mask_fname}', 'r') as h5file_mask:
    # mask = h5file_mask['/entry/data/data'][:]

# run_sum = np.zeros(mask.shape)

# with h5py.File(f'{data_fname}', 'r') as h5file_data:
    # d_shape = h5file_data['/entry/data/data'].shape


# h5file_data = h5py.File(f'{data_fname}', 'r')

# for i in range(d_shape[0]):
    # run_sum += h5file_data['/entry/data/data'][i,:,:]

# plt.figure()
# plt.imshow(run_sum)


def three_pt_centre(x1,x2,x3,y1,y2,y3):

    x12 = x1 - x2
    x13 = x1 - x3
    y12 = y1 - y2
    y13 = y1 - y3
    y31 = y3 - y1
    y21 = y2 - y1
    x31 = x3 - x1
    x21 = x2 - x1
    sx13 = x1**2 - x3**2
    sy13 = y1**2 - y3**2
    sx21 = x2**2 - x1**2
    sy21 = y2**2 - y1**2
    f = ((sx13) * (x12) + (sy13) * (x12)+ (sx21) * (x13)+ (sy21) * (x13))/ (2 * ((y31) * (x12) - (y21) * (x13)))
    g = ((sx13) * (y12) + (sy13) * (y12)+ (sx21) * (y13)+ (sy21) * (y13))/ (2 * ((x31) * (y12) - (x21) * (y13)))
    print('Center')
    print(-g, -f)






x=


three_pt_centre(1249.2, 2906.5, 2196.1, 2268.0, 2047.5, 3062.1)



# plt.show()








