import numpy as np
from matplotlib import pyplot as plt
import magpylib as magpy
import time
from scipy.spatial.transform import Rotation as R

# MAGNETIZATION WAS WRONG BY A FACTOR OF 2 AND POSITION OFFSETS WERE WRONG AS WELL!!!

M = 6335/(4*1.26) # magnetization (mT)
D = .5*25.4 # diameter (mm)
L = .75*25.4 # length (mm)
xo = .25*25.4 # x offset (mm)
yo = 1*25.4 # y offset (mm)
zo = (2.5/2)*25.4 # mm
d1 = .19 # in
d2 = .35 # in
d3 = .38 # in
d4 = .44 # in
d5 = .53 # in
d6 = .7 # in

d7 = 1.15 # in
d8 = 1.5 # in
d9 = 1.55 # in

d10 = 1.25 # in
d11 = 1.65 # in

print('Initializing sources...')
s11 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,0,-d1*25.4-zo])
#s12 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,0,-d1*25.4-zo])
s13 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,0,+d1*25.4+zo])
#s14 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,0,+d1*25.4+zo])

s21 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,1*yo,-d2*25.4-zo])
#s22 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,1*yo,-d2*25.4-zo])
s23 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,1*yo,+d2*25.4+zo])
#s24 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,1*yo,+d2*25.4+zo])

s31 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,2*yo,-d3*25.4-zo])
#s32 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,2*yo,-d3*25.4-zo])
s33 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,2*yo,+d3*25.4+zo])
#s34 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,2*yo,+d3*25.4+zo])

s41 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,3*yo,-d4*25.4-zo])
#s42 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,3*yo,-d4*25.4-zo])
s43 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,3*yo,+d4*25.4+zo])
#s44 = magpy.source.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,3*yo,+d4*25.4+zo])

s51 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,4*yo,-d5*25.4-zo])
s53 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,4*yo,+d5*25.4+zo])

s61 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,5*yo,-d6*25.4-zo])
s63 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,5*yo,+d6*25.4+zo])

s71 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[-xo,6*yo,-d7*25.4-zo])
s72 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,6*yo,-d7*25.4-zo])
s73 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[-xo,6*yo,+d7*25.4+zo])
s74 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,6*yo,+d7*25.4+zo])

s81 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[-xo,7*yo,-d8*25.4-zo])
s82 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,7*yo,-d8*25.4-zo])
s83 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[-xo,7*yo,+d8*25.4+zo])
s84 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,7*yo,+d8*25.4+zo])

s91 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[-xo,8*yo,-d9*25.4-zo])
s92 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,8*yo,-d9*25.4-zo])
s93 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[-xo,8*yo,+d9*25.4+zo])
s94 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[xo,8*yo,+d9*25.4+zo])

s101 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,9*yo,-d10*25.4-zo])
s103 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,9*yo,+d10*25.4+zo])

s111 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,10*yo,-d11*25.4-zo])
s113 = magpy.magnet.Cylinder(magnetization=[0,0,M],dimension=[D,L],position=[0,10*yo,+d11*25.4+zo])

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
					  s72,
					  s73,
					  s74,
					  s81,
					  s82,
					  s83,
					  s84,
					  s91,
					  s92,
					  s93,
					  s94,
					  s101,
					  s103,
					  s111,
					  s113)

cz.rotate(R.from_euler('y',90,degrees=True),anchor=0)

ymin = -yo #0
ymax = 12*yo
nys = 100

Y = [[0,y,0] for y in np.linspace(ymin,ymax,nys)]

time.sleep(1)

print('Calculating field...')

BYZ = cz.getB(Y)

time.sleep(1)

print('Preparing plots...')
ys = np.linspace(ymin,ymax,nys)
plt.figure()
plt.plot(ys/10,BYZ[:,0]*10)

B0 = 537 # Gs
L0 = 26.6 # cm
calc = B0/2*(1-ys/(L0*10))**(1/2)
plt.plot(ys/10,calc,color='r',linestyle='--')


h = .2
flng = 6 # in
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
plt.axvline(flng*2.54,ymin=0,ymax=.1,color='y')
plt.axvline((flng+2)*2.54,ymin=0,ymax=.1,color='y')

plt.title('Magnetic Field Intensity Along Beamline')
plt.xlabel('Beamline Location (cm)')
plt.ylabel('Magnetic Field (Gs)')


plt.figure(figsize=(8,8))
xs = np.linspace(-5*25.4,5*25.4,100)
Btot = np.array([[cz.getB([x,y,0]) for x in xs] for y in ys])
Xm,Ym = np.meshgrid(xs,ys)
U,V = Btot[:,:,0], Btot[:,:,1]
plt.pcolor(xs,ys,np.log(U**2+V**2))
plt.streamplot(Xm,Ym,U,V,color='w',density=2)
plt.margins(0,0)

magpy.show(cz)

print('FINISHED')
plt.show()