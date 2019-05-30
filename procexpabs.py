# -*- coding: utf-8 -*-
"""
Accepts experimental UV-vis spectrum data as an input and converts wavelength
to transition energy for experimental fitting via ORCA quantum chemistry 
package. 

Input is given as a .txt file formatted as so:
"Wavelength (nm)"	"Absorbance (AU)"
     190.0	     0.762002
     191.0	     0.885745
     192.0	     1.166660
     ...         ...
     etc.

Intensities are converted to molar extinction coefficients for accurate
fitting of transition dipole moments and oscillator strengths.
"""
import numpy as np #needed for matrix operations 


filepath = input("Input file path of raw experimental spectrum to be fit: \n")
concentration = float(input("Concentration (M): \n"))
pathlength = float(input("Pathlength (cm): \n"))


a,b = np.loadtxt(filepath, skiprows=1, unpack=True) #a is wavelength, b absorbance
a = np.divide(10000000,a) #converts nm to cm^-1
b = np.divide(b,(pathlength*concentration))
c = np.transpose([a, b])

i = len(filepath)
outputtemp = filepath[:(i - 4)]
output = outputtemp + "_out.txt"

np.savetxt(output, c, fmt="%d", delimiter=" ")

print("\nProcessed spectral data for ORCA input generated.")