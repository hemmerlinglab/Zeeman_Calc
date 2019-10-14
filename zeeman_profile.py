'''Page 183 in the Foot book for equations'''
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
amu    = 1.66054*10**(-27)



def calc_L0(opts):

	vel = opts['v0']
	eta = opts['eta']
	accel = calc_a_max(opts)

	return vel**(2)/(accel*eta)

def calc_a_max(opts):

	lamb = opts['lambda']
	gamma = opts['gamma']
	m = opts['mass']
	return h/lamb*gamma/(2*m)

def gJ(S, L, J):

	gL = 1.0
	gS = 2.0

	if J == 0:
		return 0.0
	else:
		return gL * (J * (J+1) - S*(S+1) + L*(L+1))/(2*J*(J+1)) + gS * (J * (J+1) + S*(S+1) - L*(L+1))/(2*J*(J+1))

def calc_B0(opts):

	k = 2*np.pi/opts['lambda']
	v0 = opts['v0']

	mJ_g = opts['J_g'] # setting mJ = J
	mJ_e = opts['J_e']

	gJ_g = gJ(opts['S_g'], opts['L_g'], opts['J_g'])
	gJ_e = gJ(opts['S_e'], opts['L_e'], opts['J_e'])

	return hbar*k*v0/((mJ_e*gJ_e - mJ_g*gJ_g)*muB)

def plot_zeeman(opts):
	
	B0 = calc_B0(opts)
	L0 = calc_L0(opts)

	start_z = 0
	end_z   = L0
	steps   = 200
	z       = np.linspace(start_z,end_z,steps)

	Bfield = B0 * np.sqrt(1-z/L0)
	
	plt.figure()
	plt.plot(z*1e2,Bfield*1e4,'k')

	plt.tick_params(labelsize=16) #tick size
	plt.tick_params(direction='in') #tick direction

	plt.xlabel('z (cm)',fontsize=16)
	plt.ylabel('Magnetic Field (gauss)',fontsize=16)
	
	plt.title(opts['name'] + ' Zeeman Slower - max velocity: ' +  str(opts['v0']) + 'm/s', fontsize=16)	

	plt.text(0,0, 'B0 = ' + str(round(B0*1e4)) + ' Gs; L0 = ' + str(round(L0*1e2)) + ' cm')

	plt.tight_layout()




'''Yb Variables'''

yb_opts = {
	'name' : 'Yb',
	'mass' : 174*amu,
	'v0' : 300,
	'lambda' : 398.9e-9,
	'gamma' : 2*np.pi * 28.0e6,
	'S_g' : 0,
	'L_g' : 0,
	'J_g' : 0,
	'S_e' : 0,
	'L_e' : 1,
	'J_e' : 1,
	'eta' : 0.67
	}
	 

mo_opts = {
	'name' : 'Mo',
	'mass' : 100*amu,
	'v0' : 300,
	'lambda' : 374.825e-9,
	'gamma' : 2*np.pi * 11.0e6,
	'S_g' : 3,
	'L_g' : 0,
	'J_g' : 3,
	'S_e' : 3,
	'L_e' : 1,
	'J_e' : 4,
	'eta' : 0.67
	}


na_opts = {
	'name' : 'Na',
	'mass' : 23*amu,
	'v0' : 1000,
	'lambda' : 589e-9,
	'gamma' : 6.16e7,
	'S_g' : 1.0/2.0,
	'L_g' : 0,
	'J_g' : 1.0/2.0,
	'S_e' : 1.0/2.0,
	'L_e' : 1.0,
	'J_e' : 3.0/2.0,
	'eta' : 1.0
	}




plot_zeeman(yb_opts)

plot_zeeman(mo_opts)

plot_zeeman(na_opts)

plt.show()
