import scipy
import numpy as np
from scipy.optimize import fsolve
import time

# z - axis is zaxis of magnet (perpendicular to beamline)
# y - beamline

# M - magnetization, obtained from magnets.py
M = 4*6335 # uo*M/2
R = .25*25.4e-3 # radius of magnet in meters
L = .75*25.4e-3 # length of magnet in meters
nmags = 8 # number of positions of magnets along the beamline
B0 = 268 # Gs
L0 = .118 # stopping distance- obtained from zeeman.py
switch_point = 6 # from stacked to unstacked, index in the array which you swtich from being stacked to not stacked
ys = np.linspace(0,L0,nmags+1)[:-1] # ensures L0 is not included in the ys

sols = [] # solution array
ni = len(ys) # number of points , len of y

# going through every point on the y
for i in range(ni):
	def Zeeman(z):
		if i < switch_point:
			# cylindrical magnet equation has to be equal to the required zeeman profile
			return M*(z/np.sqrt(z**2+R**2)-(z-L)/np.sqrt((z-L)**2+R**2))-B0*(1-ys[i]/L0)
		else:
			return M/2*(z/np.sqrt(z**2+R**2)-(z-L)/np.sqrt((z-L)**2+R**2))-B0*(1-ys[i]/L0)
	test = [.03] # start looking here for a fit
	roots = fsolve(Zeeman,test) # function for finding roots
	sols.append(roots[0]-L) # append the solution, solve for roots, subtract length of magnet
	
	# john messing around with progress bars
	n = (80*(i+1)//ni)
	print('[{}{}] {}%'.format('|'*n,' '*(80-n),100*(i+1)//ni),end='\r')
	time.sleep(.1)

print(' '*125)
rmin = 2.5*2.54/2 # min length in cm that the magnet cn be (cannot go through vacuum chamber)
smin = 2*R*100 # minimum spacing, makes sure the magnets are not going through each other
# converts from m to cm
spacing = L0*100/(nmags+1) # figuring out the actual spacing between magnets
print('Total Number of Magnets: {}'.format(4*switch_point+2*(nmags-switch_point)))

# when te transition happens
print('Transition from 2 -> 1 magnets per side: {} -> {}'.format(switch_point,switch_point+1))
print('Minimum spacing: {} cm'.format(smin))
print('Magnet spacing: {} cm'.format(spacing))
print('Minimum radius: {} cm'.format(rmin))
print('Total Slower Length: {} cm'.format((nmags*L0/(nmags+1)+2*R)*100)) #min size of mechanical thing
for j in range(len(sols)):
	if j == 0:
		print('\n- 2 Magnets on Each Side')
	elif j == switch_point:
		print('- 1 Magnet on Each Side')
	print('Magnet {} ({}): {} cm'.format(j+1,ys[j]*100/2.54,sols[j]*100))
print('\nSimulation Successful: {}'.format(np.min(sols)*100>rmin and spacing>smin))