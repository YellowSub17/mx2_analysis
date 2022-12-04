clen = 0.1996

photon_energy = 13000

adu_per_photon = 1
res = 13333.3   ; 75 micron pixel size

; These lines describe the data layout for the Eiger native multi-event files
dim0 = %
dim1 = ss
dim2 = fs
data = /entry/data/data



rigid_group_d0 = panel0
rigid_group_collection_det = d0

; corner_{x,y} set the position of the corner of the detector (in pixels)
; relative to the beam

panel0/min_fs = 0 
panel0/min_ss = 0 
panel0/max_fs = 99
panel0/max_ss = 99
panel0/corner_x = 0
panel0/corner_y = 0
panel0/fs = +1.000000x +0.000000y 
panel0/ss = +0.000000x +1.000000y





