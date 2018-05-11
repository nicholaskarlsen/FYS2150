#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nicholas karlsen

import numpy as np
import matplotlib.pyplot as plt

d = 846.7e-9    # Gitterkonstant

# Helium lines in order
# Red, yellow, green1, green2, green3, blue, purple
He_av = np.array([144.4, 152.8, 160.4, 160.6, 161.5, 163.2, 165.2])
He_ah = np.array([248.7, 240.9, 233.7, 233.4, 232.7, 231.0, 229.1])

# Hydrogen lines in order
# Purple, green, red
H_av = np.array([167.4, 163.1, 146.1])
H_ah = np.array([228.8, 223.3, 248.8])

He_theta = (He_ah - He_av) / 2.0
H_theta = (H_ah - H_av) / 2.0


def wlen(theta):
    return d * np.sin(np.deg2rad(theta))


H_wlen = wlen(H_theta)
He_wlen = wlen(He_theta)



def dTheta(dah=0.01, dav=0.01):
    "error in measured angle"
    return 0.5 * np.sqrt(dah**2 + dav**2)


def dWlen(theta, Wlen, d_err=1E-9):
    "Error in measured wavelength"
    a = d_err / d
    b = dTheta() / np.tan(theta)
    return Wlen * np.sqrt(a**2 + b**2)


def balmerlines(last_n):
    R = 1.097E7    # Rydberg constant
    n = np.linspace(3, last_n, last_n - 3)
    return 1.0 / (R * (0.5**2 - (1.0 / n)**2))

print "Balmer lines", balmerlines(10)
print
print "Helium lines", He_wlen
print
print "-------------"
print "Hydrogen lines", H_wlen


plt.scatter(H_wlen, np.zeros_like(H_wlen), 
            label="Observed Hydrogen lines", color="r")
plt.scatter(balmerlines(20), np.zeros_like(balmerlines(20)) + 0.5, 
            label="Predicted Balmer lines", color="black")
plt.xlim(400E-9, 700E-9)
plt.yticks([])
plt.legend()
plt.close()


def hydrogen_table():
    outfile = open("dat/hydrogenlines.dat", "w")
    outfile.write("$\\alpha_v$ & $\\alpha_h$ & $\\theta$ & $\\lambda$ [nm]")
    outfile.write("\n")
    outfile.write("\\\\ \\hline ")
    for i in range(len(H_ah)):
        outfile.write("$%.2f \\pm 0.01 ^\\circ$" % H_av[i])
        outfile.write(" & ")
        outfile.write("$%.2f \\pm 0.01^\\circ$" % H_ah[i])
        outfile.write(" & ")
        outfile.write("$%.2f \\pm %.2f^\\circ$" % (H_theta[i], dTheta()))
        outfile.write(" & ")
        outfile.write("$%.2f \\pm %.2f$" % (H_wlen[i] * 1e9, dWlen(H_theta[i], H_wlen[i]) * 1e9))
        outfile.write(" \\\\")
    outfile.close()

hydrogen_table()