# Zeeman_Calc
Code for calculation involved in building a Zeeman slower.
##zeeman_calc.py
Programmed by Kayla, based on paper (Kayla add more)
##zeeman_slower_v2.py
###Intro
Programmed by John.  Using the fit function that was used in the Magnet_Measurement repository and the values obtained therein, the scipy.optimize.fsolve function was used to optimize the expected positions for the magnets.
###Solution
The value of M that is obtained is half the multiple of M (the magnetic dipole density of the ferromagnet), the magnetic permeability of free space constant.  The basic form of the equation that is optimized is B_mag - B_zeeman = 0.  The output is the positions of the magnets.  The value of M is multiplied by a factor of 2 when there is only one magnet on each side (double the field on the beam axis) and a factor of 4 when there are two vertically stacked magnets on each side.  The transition from stacked to unstacked magnets can be easily adjusted.