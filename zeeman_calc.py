'''Page 183 in the Foot book'''



import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import csv
import datetime
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
import pylab as plb



'''Global variables'''

muB    = 9.274009994*10**(-24) # bohr magneton in SI units
c      = 299792458 
h      = 6.62607004*10**(-34) # Energy in Joules * s
hbar   = h/(2*np.pi)

'''Yb Variables'''

M      = 173*1.66054*10**(-27) # mass in kg
v0     = 100   # m/s
lbda   = 398.9*10**(-9) # meters
gamma  = 28*10**(6)*2*np.pi # decay rate Yb
k      = 2*np.pi/(lbda)
a_max  = hbar*k*gamma/(2*M)


eta = .67

# Quantum numbers stuff

me1     = 1  # magnetic quantum number excited state
me_1    = -1
me0     = 0
mg      = 0  # magnetic quantum number ground state
ge      = 1 # Lande g factor excited state
gg      = 0  # Lande g factor ground state
mueff1  = (me1*ge - mg*gg)*muB
mueff_1 = (me_1*ge - mg*gg)*muB



''' Mo Variables '''

M_mo     = 100*1.66054*10**(-27) # mass in kg
v0_mo    = 150   # m/s
lbda_mo  = 390.9*10**(-9) # meters
gamma_mo = 11*10**(6)*2*np.pi # decay rate Mo
k_mo     = 2*np.pi/(lbda_mo)
a_max_mo = hbar*k_mo*gamma_mo/(2*M_mo)

# Quantum numbers stuff

me1_mo     = 1 # magnetic quantum number excited state
me_1_mo    = -1
me0_mo     = 0
mg_mo      = 0 # magnetic quantum number ground state
ge_mo      = 7/3 # Lande g factor excited state
gg_mo      = 2 # Lande g factor ground state
mueff1_mo  = (me1_mo*ge_mo - mg_mo*gg_mo)*muB
mueff_1_mo = (me_1_mo*ge_mo - mg_mo*gg_mo)*muB

# depends on laser intensity 
I      = 1      # laser intensity
I_sat  = 0.147      # saturation intensity mW cm^-1
s      = I/I_sat
eta_eq = s/(1+s)

eta_mo = 0.67

'''Zeeman params for yb'''
B01  = hbar*k*v0/(mueff1)  #initial B field for m = 1
B0_1 = hbar*k*v0/(mueff_1) #initial B field for m = -1

L0      = v0**(2)/(2*eta*a_max)     # stopping distance
start_z = 0
end_z   = L0
steps   = 200
z       = np.linspace(start_z,end_z,steps)
B1      = B01*(1-z/L0)**(1/2)
B_1     = B0_1*(1-z/L0)**(1/2)


print('params for yb:')
print('L0: '    + str(L0)) 
print('B01: gauss '    + str(B01*1e4))
print('B0_1: gauss '   + str(B0_1*1e4))
print('a_max: ' + str(a_max)) 

'''Zeeman params for moly'''
B01_mo  = hbar*k_mo*v0_mo/(mueff1_mo)  #initial B field for m = 1
B0_1_mo = hbar*k_mo*v0_mo/(mueff_1_mo) #initial B field for m = -1

L0_mo      = v0_mo**(2)/(2*eta_mo*a_max_mo)     # stopping distance
start_z_mo = 0
end_z_mo   = L0_mo
steps_mo   = 200
z_mo       = np.linspace(start_z_mo,end_z_mo,steps_mo)
B1_mo      = B01_mo*(1-z_mo/L0_mo)**(1/2)
B_1_mo     = B0_1_mo*(1-z_mo/L0_mo)**(1/2)


print('params for mo:')
print('L0_mo: '    + str(L0_mo)) 
print('B01_mo: gauss '    + str(B01_mo*1e4))
print('B0_1_mo: gauss '   + str(B0_1_mo*1e4))
print('a_max_mo: ' + str(a_max_mo)) 


'''yb plot params'''
plt.plot(z*1e2,B1*1e4,'m',label='m=1')
plt.tick_params(labelsize=16) #tick size
plt.tick_params(direction='in') #tick direction
plt.xlabel('z (cm)',fontsize=16)
plt.ylabel('Magnetic Field (gauss)',fontsize=16)
plt.plot(z*1e2,B_1*1e4,'b',label='m =-1')
plt.title('yb zeeman slower',fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()

''' Moly plot params '''
plt.figure()
plt.plot(z_mo*1e2,B1_mo*1e4,'m',label='m=1')
plt.tick_params(labelsize=16) #tick size
plt.tick_params(direction='in') #tick direction
plt.xlabel('z (cm)',fontsize=16)
plt.ylabel('Magnetic Field (gauss)',fontsize=16)
plt.plot(z_mo*1e2,B_1_mo*1e4,'b',label='m =-1')
plt.title('mo zeeman slower',fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()


plt.show()
