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
hbar   = h*2*np.pi

'''Yb Variables'''

M      = 173*1.66054*10**(-27)
v0     = 150   # m/s
lbda   = 398.9 # nm
gamma  = 28*10**(-6)*2*np.pi # decay rate Yb
freq   = 391 # THz
k      = 2*np.pi/lbda
a_max  = hbar*k*gamma/(2*M)

'''Zeeman params'''
B0 = h*v0/(lbda*muB) #initial B field
L0 = v0**(2)/a_max     # stopping distance
start_z = 0
end_z   = 15
steps   = 50
z       = np.linspace(start_z,end_z,steps)
B       = B0*(1+z/L0)**(1/2)


