import numpy as np
from matplotlib import pyplot as plt
import magpylib as magpy
import time

M = 6335/(2*1.26) # magnetization (mT)
D = .5*25.4 # diameter (mm)
L = .75*25.4 # length (mm)
xo = .25*25.4 # x offset (mm)
yo = 1*25.4 # y offset (mm)
zo = (2.5/2)*25.4
d1 = .003
d2 = .077
d3 = .165
d4 = .276
d5 = .3
d6 = .4
d7 = .421
d8 = .6
d9 = .948
d10 = .948
d11 = 1.2

print('Initializing sources...')
s11 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,0,-d1*25.4-zo])
#s12 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,0,-d1*25.4-zo])
s13 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,0,+d1*25.4+zo])
#s14 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,0,+d1*25.4+zo])

s21 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,1*yo,-d2*25.4-zo])
#s22 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,1*yo,-d2*25.4-zo])
s23 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,1*yo,+d2*25.4+zo])
#s24 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,1*yo,+d2*25.4+zo])

s31 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,2*yo,-d3*25.4-zo])
#s32 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,2*yo,-d3*25.4-zo])
s33 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,2*yo,+d3*25.4+zo])
#s34 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,2*yo,+d3*25.4+zo])

s41 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,3*yo,-d4*25.4-zo])
#s42 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,3*yo,-d4*25.4-zo])
s43 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,3*yo,+d4*25.4+zo])
#s44 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,3*yo,+d4*25.4+zo])

s51 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,4*yo,-d5*25.4-zo])
s53 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,4*yo,+d5*25.4+zo])

s61 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,5*yo,-d6*25.4-zo])
s63 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,5*yo,+d6*25.4+zo])

s71 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,6*yo,-d7*25.4-zo])
s73 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,6*yo,+d7*25.4+zo])

s81 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,7*yo,-d8*25.4-zo])
s83 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,7*yo,+d8*25.4+zo])

s91 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,8*yo,-d9*25.4-zo])
s93 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,8*yo,+d9*25.4+zo])

s101 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,9*yo,-d10*25.4-zo])
s103 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,9*yo,+d10*25.4+zo])

s111 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,10*yo,-d11*25.4-zo])
s113 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,10*yo,+d11*25.4+zo])

time.sleep(1)

print('Initializing collections...')
#c1 = magpy.Collection(s11,s12,s13,s14)
#c2 = magpy.Collection(s21,s22,s23,s24)
#c3 = magpy.Collection(s31,s32,s33,s34)
#c4 = magpy.Collection(s41,s42,s43,s44)
#c5 = magpy.Collection(s51,s53)
#c6 = magpy.Collection(s61,s63)
#c7 = magpy.Collection(s71,s73)
#c8 = magpy.Collection(s81,s83)

cz = magpy.Collection(s11,
					  #s12,
					  s13,
					  #s14,
					  s21,
					  #s22,
					  s23,
					  #s24,
					  s31,
					  #s32,
					  s33,
					  #s34,
					  s41,
					  #s42,
					  s43,
					  #s44,
					  s51,
					  s53,
					  s61,
					  s63,
					  s71,
					  s73,
					  s81,
					  s83,
					  s91,
					  s93,
					  s101,
					  s103,
					  s111,
					  s113)

ymin = 0
ymax = 11*yo
nys = 100

Y = [[0,y,0] for y in np.linspace(ymin,ymax,nys)]

time.sleep(1)

print('Calculating field...')

BYZ = cz.getBsweep(Y)

time.sleep(1)

print('Preparing plots...')
ys = np.linspace(ymin,ymax,nys)
plt.figure()
plt.plot(ys/10,BYZ[:,2]*10)

B0 = 537 # Gs
L0 = 26.6 # cm
calc = B0*(1-ys/(L0*10))**(1/2)
plt.plot(ys/10,calc,color='r',linestyle='--')


h = .2
plt.axvline(0,ymin=0,ymax=h,color='g')
plt.axvline(.1*yo,ymin=0,ymax=h,color='g')
plt.axvline(.2*yo,ymin=0,ymax=h,color='g')
plt.axvline(.3*yo,ymin=0,ymax=h,color='g')
plt.axvline(.4*yo,ymin=0,ymax=h,color='g')
plt.axvline(.5*yo,ymin=0,ymax=h,color='g')
plt.axvline(.6*yo,ymin=0,ymax=h,color='g')
plt.axvline(.7*yo,ymin=0,ymax=h,color='g')
plt.axvline(.8*yo,ymin=0,ymax=h,color='g')
plt.axvline(.9*yo,ymin=0,ymax=h,color='g')
plt.axvline(yo,ymin=0,ymax=h,color='g')

plt.title('Magnetic Field Intensity Along Beamline')
plt.xlabel('Beamline Location (cm)')
plt.ylabel('Magnetic Field (Gs)')


# plt.figure(figsize=(8,8))
# zs = np.linspace(-5*25.4,5*25.4,100)
# Btot = np.array([[cz.getB([0,y,z]) for y in ys] for z in zs])
# Ym,Zm = np.meshgrid(ys,zs)
# U,V = Btot[:,:,1], Btot[:,:,2]
# plt.pcolor(ys,zs,np.log(U**2+V**2))
# plt.streamplot(Ym,Zm,U,V,color='w',density=2)
# plt.margins(0,0)


cz.displaySystem()

print('FINISHED')
plt.show()