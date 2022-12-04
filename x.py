

import h5py
import hdf5plugin

h5file = h5py.File('./testrun12/testcrystal_0012_data_000012.h5','r')



d = h5file['entry/data/data'][0, :]

h5file.close()
