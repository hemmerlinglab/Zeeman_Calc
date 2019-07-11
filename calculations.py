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
lbda   = 400 # nm
freq   = 391 # THz
muB    = 1 
c      = 299792458 
h      = 6.62607004*10**(-34) # Energy in Joules * s
M      = 173*1.66054*10**(-27)
M_mo   = 95.95*1.66054*10**(-27)
gamma  = 1 # decay rate
hbar   = h*2*np.pi
a_max  = hbar*k*gamma/(2*M)

B0 = h*v0*freq/(c*muB) #initial B field
L0 = v0**(2)/a_max


