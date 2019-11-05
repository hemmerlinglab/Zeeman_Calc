import numpy as np
import matplotlib.pyplot as plt
import magpylib as magpy

M = 6335/(4*1.26) # magnetization (mT)
D = .5*25.4 # diameter (mm)
L = .75*25.4 # length (mm)

def Cylmag(loc,ori,d=D,l=L,m=M):
	return magpy.source.magnet.Cylinder(mag=[0,0,ori*m],dim=[d,l],pos=loc)

ylocs = np.arange(0,11)*25.4 # mm, beam line locations
zoffset = (2.5/2+.375)*25.4 # mm, radius of nipple plus half the magnet
zlocs = [0,0,0,0,0,0,0,0,0,0,0] # mm, radial distances
xoffset = .25*25.4 # mm, magnet radius for double stacked
oris = [1,1,1,1,1,1,1,1,-1,-1,-1]

sources = {}

for i in range(11):
	if i in range(6,9):
		sources['{}tr'.format(i)] = Cylmag(loc=[xoffset,ylocs[i],zlocs[i]+zoffset],ori=oris[i])
		sources['{}br'.format(i)] = Cylmag(loc=[-xoffset,ylocs[i],zlocs[i]+zoffset],ori=oris[i])
		sources['{}tl'.format(i)] = Cylmag(loc=[xoffset,ylocs[i],-zlocs[i]-zoffset],ori=oris[i])
		sources['{}bl'.format(i)] = Cylmag(loc=[-xoffset,ylocs[i],-zlocs[i]-zoffset],ori=oris[i])
	else:
		sources['{}r'.format(i)] = Cylmag(loc=[0,ylocs[i],zlocs[i]+zoffset],ori=oris[i])
		sources['{}l'.format(i)] = Cylmag(loc=[0,ylocs[i],-zlocs[i]-zoffset],ori=oris[i])

C = magpy.Collection()

for sc in sources:
	C.addSources(sources[sc])


ymin = -1*25.4 # mm
ymax = 11*25.4 # mm
ny = 100
ys = np.linspace(ymin,ymax,ny)
Y = [[0,y,0] for y in ys]
BZy = C.getBsweep(Y) # mT

plt.figure()
plt.plot(ys/25.4,BZy[:,2]*10)
plt.xlabel('Beamline Position (in)')
plt.ylabel('Z Magnetic Field (Gs)')
plt.title('Beamline Z Magnetic Field')


zmin = -100 # mm
zmax = 100 # mm
nz = 100
zs = np.linspace(zmin,zmax,nz)
Z = [[0,0,z] for z in zs]
BZz = C.getBsweep(Z) # mT

plt.figure()
plt.plot(zs/25.4,BZz[:,2]*10)
plt.axvline(zoffset/25.4+.375)
plt.axvline(zoffset/25.4-.375)
plt.axvline(-zoffset/25.4+.375)
plt.axvline(-zoffset/25.4-.375)
plt.xlabel('Z Position (in)')
plt.ylabel('Z Magnetic Field (Gs)')
plt.title('Cross Beam Z Magnetic Field')


C.displaySystem()

plt.show()