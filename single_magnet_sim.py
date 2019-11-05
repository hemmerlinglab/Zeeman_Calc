import numpy as np
import magpylib as magpy
from matplotlib import pyplot as plt

M = 6335/(4*1.26) # magnetization (mT)
D = .5*25.4 # diameter (mm)
L = .75*25.4 # length (mm)

s1 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,0,0])

zmin = -75 # mm
zmax = 75 # mm
nz = 100

Z = [[0,0,z] for z in np.linspace(zmin,zmax,nz)]

BZ = s1.getBsweep(Z)

zs = np.linspace(zmin,zmax,nz)/25.4

plt.figure()
plt.plot(zs,BZ[:,2]*10)
plt.xlabel('Z Position (in)')
plt.ylabel('Magnetic Field (Gs)')
plt.title('Single Magnet Z-Axis B-Field')
plt.axvline(.375)
plt.axvline(-.375)
plt.show()
