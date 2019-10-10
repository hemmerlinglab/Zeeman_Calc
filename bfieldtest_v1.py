import numpy as np
from matplotlib import pyplot as plt
import magpylib as magpy
import time

M = 6335/(2*1.26) # magnetization (mT)
D = .5*25.4 # diameter (mm)
L = .75*25.4 # length (mm)
xo = .25*25.4 # x offset (mm)
yo = .58*25.4 # y offset (mm)
zo = (2.5/2)*25.4

print('Initializing sources...             ',end='\r')
s11 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,0,-.003*25.4-zo-L])
s12 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,0,-.003*25.4-zo-L])
s13 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,0,+.003*25.4+zo])
s14 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,0,+.003*25.4+zo])

s21 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,1*yo,-.077*25.4-zo-L])
s22 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,1*yo,-.077*25.4-zo-L])
s23 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,1*yo,+.077*25.4+zo])
s24 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,1*yo,+.077*25.4+zo])

s31 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,2*yo,-.165*25.4-zo-L])
s32 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,2*yo,-.165*25.4-zo-L])
s33 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,2*yo,+.165*25.4+zo])
s34 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,2*yo,+.165*25.4+zo])

s41 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,3*yo,-.276*25.4-zo-L])
s42 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,3*yo,-.276*25.4-zo-L])
s43 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[-xo,3*yo,+.276*25.4+zo])
s44 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[xo,3*yo,+.276*25.4+zo])

s51 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,4*yo,-.0025*25.4-zo-L])
s53 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,4*yo,+.0025*25.4+zo])

s61 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,5*yo,-.164*25.4-zo-L])
s63 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,5*yo,+.164*25.4+zo])

s71 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,6*yo,-.421*25.4-zo-L])
s73 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,6*yo,+.421*25.4+zo])

s81 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,7*yo,-.948*25.4-zo-L])
s83 = magpy.source.magnet.Cylinder(mag=[0,0,M],dim=[D,L],pos=[0,7*yo,+.948*25.4+zo])

time.sleep(1)

print('Initializing collections...          ',end='\r')
c1 = magpy.Collection(s11,s12,s13,s14)
c2 = magpy.Collection(s21,s22,s23,s24)
c3 = magpy.Collection(s31,s32,s33,s34)
c4 = magpy.Collection(s41,s42,s43,s44)
c5 = magpy.Collection(s51,s53)
c6 = magpy.Collection(s61,s63)
c7 = magpy.Collection(s71,s73)
c8 = magpy.Collection(s81,s83)

cz = magpy.Collection(s11,s12,s13,s14,
					  s21,s22,s23,s24,
					  s31,s32,s33,s34,
					  s41,s42,s43,s44,
					  s51,s53,s61,s63,
					  s71,s73,s81,s83)

ymin = -yo
ymax = 9*yo
nys = 100

Y = [[0,y,0] for y in np.linspace(ymin,ymax,nys)]

time.sleep(1)

print('Calculating field...           ',end='\r')
BY1 = c1.getBsweep(Y)
BY2 = c2.getBsweep(Y)
BY3 = c3.getBsweep(Y)
BY4 = c4.getBsweep(Y)
BY5 = c5.getBsweep(Y)
BY6 = c6.getBsweep(Y)
BY7 = c7.getBsweep(Y)
BY8 = c8.getBsweep(Y)

BYZ = cz.getBsweep(Y)
#plt.figure()
#plt.plot(BY1[:,2])

#plt.figure()
#plt.plot(BY2[:,2])

time.sleep(1)

print('Preparing plots...            ',end='\r')
ys = np.linspace(ymin,ymax,nys)
plt.figure()
plt.plot(ys,BYZ[:,2])
#plt.plot(ys,BY1[:,2],color='r',linestyle='--')
#plt.plot(ys,BY2[:,2],color='r',linestyle='--')
#plt.plot(ys,BY3[:,2],color='r',linestyle='--')
#plt.plot(ys,BY4[:,2],color='r',linestyle='--')
#plt.plot(ys,BY5[:,2],color='r',linestyle='--')
#plt.plot(ys,BY6[:,2],color='r',linestyle='--')
#plt.plot(ys,BY7[:,2],color='r',linestyle='--')
#plt.plot(ys,BY8[:,2],color='r',linestyle='--')
h = .2
plt.axvline(0,ymin=0,ymax=h,color='g')
plt.axvline(1*yo,ymin=0,ymax=h,color='g')
plt.axvline(2*yo,ymin=0,ymax=h,color='g')
plt.axvline(3*yo,ymin=0,ymax=h,color='g')
plt.axvline(4*yo,ymin=0,ymax=h,color='g')
plt.axvline(5*yo,ymin=0,ymax=h,color='g')
plt.axvline(6*yo,ymin=0,ymax=h,color='g')
plt.axvline(7*yo,ymin=0,ymax=h,color='g')


plt.figure(figsize=(8,8))
zs = np.linspace(-5*25.4,5*25.4,100)
Btot = np.array([[cz.getB([0,y,z]) for y in ys] for z in zs])
Ym,Zm = np.meshgrid(ys,zs)
U,V = Btot[:,:,1], Btot[:,:,2]
plt.pcolor(ys,zs,np.log(U**2+V**2))
plt.streamplot(Ym,Zm,U,V,color='w',density=2)
plt.margins(0,0)


cz.displaySystem()

print('FINISHED                     ')
plt.show()