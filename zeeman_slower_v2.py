import scipy
import numpy as np
from scipy.optimize import fsolve

M = 4*6335 # uo*M/2
R = .25*25.4e-3 # m
L = .75*25.4e-3 # m
nmags = 10
B0 = 268 # Gs
L0 = .3 # m
switch_point = 5 # from stacked to unstacked
ys = np.linspace(0,L0,nmags+1)[:-1] # m

sols = []
ni = len(ys)

for i in range(ni):
	def Zeeman(z):
		if i < switch_point:
			return M*(z/np.sqrt(z**2+R**2)-(z-L)/np.sqrt((z-L)**2+R**2))-B0*(1-ys[i]/L0)
		else:
			return M/2*(z/np.sqrt(z**2+R**2)-(z-L)/np.sqrt((z-L)**2+R**2))-B0*(1-ys[i]/L0)
	test = [.03]
	roots = fsolve(Zeeman,test)
	sols.append(roots[0]-L)
	n = (100*(i+1)//ni)
	print('[{}{}] {}'.format('|'*n,' '*(100-n),100*(i+1)/ni),end='\r')
print(' '*120)
rmin = 2.5*2.54/2
print('Minimum spacing: {} cm'.format(2*R*100))
print('Magnet spacing: {} cm'.format(L0*100/(nmags+1)))
print('Minimum radius: {} cm'.format(rmin))
print('Total Slower Length: {} cm'.format((nmags*L0/(nmags+1)+2*R)*100))
for j in range(len(sols)):
	if j == 0:
		print('- 2 Magnets on Each Side')
	elif j == switch_point:
		print('- 1 Magnet on Each Side')
	print('Magnet {}: {} cm'.format(j+1,sols[j]*100))
print('Simulation Successful: {}'.format(np.min(sols)*100>rmin))