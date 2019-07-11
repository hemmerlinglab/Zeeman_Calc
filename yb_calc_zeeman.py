import numpy as np
import matplotlib

matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt
import csv
import datetime
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
import pylab as plb

v0     = 150   # m/s
lbda   = 398.9 # nm
freq   = 391 # THz
muB    = 9.274009994*10**(-24) # bohr magneton in SI units
c      = 299792458 
h      = 6.62607004*10**(-34) # Energy in Joules * s
M      = 173*1.66054*10**(-27)
M_mo   = 95.95*1.66054*10**(-27)
gamma  = 28*10**(-6)*2*np.pi # decay rate
hbar   = h*2*np.pi
a_max  = hbar*k*gamma/(2*M)
k      = 2*np.pi/lbda

B0 = h*v0/(lbda*muB) #initial B field
L0 = v0**(2)/a_max     # stopping distance

start_z = 0
end_z   = 15
steps   = 50
z       = linspace(start_z,end_z,steps)
B       = B0*(1+z/L0)**(1/2)


