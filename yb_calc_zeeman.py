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
v0     = 150   # m/s
lbda   = 398.9*10**(-9) # meters
gamma  = 28*10**(6)*2*np.pi # decay rate Yb
k      = 2*np.pi/(lbda)
a_max  = hbar*k*gamma/(2*M)

# Quantum numbers stuff

# double check the me number 

me     = 1 # magnetic quantum number excited state
mg     = 0 # magnetic quantum number ground state
ge     = 1 # Lande g factor excited state
gg     = 0 # Lande g factor ground state
mueff   = (me*ge - mg*gg)/muB


'''Zeeman params'''
B0 = hbar*k*v0/(mueff) #initial B field
L0 = v0**(2)/a_max     # stopping distance
start_z = 0
end_z   = 15
steps   = 50
z       = np.linspace(start_z,end_z,steps)
B       = B0*(1+z/L0)**(1/2)

print('params:')
print('L0: '    + str(L0)) 
print('B0: '    + str(B0))
print('a_max: ' + str(a_max)) 
print('hbar ' + str(hbar))
print('k    ' + str(k))

plt.plot(z,B)
plt.tick_params(labelsize=16) #tick size
plt.tick_params(direction='in') #tick direction
plt.xlabel('z',fontsize=16)
plt.ylabel('B',fontsize=16)
plt.show()
