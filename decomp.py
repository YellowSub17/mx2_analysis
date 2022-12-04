
import h5py
import hdf5plugin
import sys
import numpy as np
import matplotlib.pyplot as plt


fname = sys.argv[1]

if fname[-3:]=='.h5':
    fname = fname[-3:]





h5file = h5py.File(f'{fname}.h5','r')
d = h5file['entry/data/data'][:, :, :]
h5file.close()


h5file_mask = h5py.File(f'/media/pat/datadrive/mx2tape/mask.h5', 'r')
mask = h5file_mask['entry/data/data'][:]
h5file_mask.close()



# d_masked = np.zeros(d.shape)

for i, frame in enumerate(d):
    print(i)
    d[i] = mask*frame





h5file_decomp = h5py.File(f'{fname}_decomp.h5','w')
h5file_decomp['entry/data/data'] = d
h5file_decomp.close()

plt.show()


