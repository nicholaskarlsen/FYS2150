#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nicholas karlsen
import numpy as np
import matplotlib.pyplot as plt


def illuminance(x, lambd,R=1, a=846.7e-9, N=3e4, A=1e-7):
    """
    Returns the illuminance, E_N.
    R = separation between slit and obersvation plane
    a = width of slit
    N = number of slits
    A = distance between slits
    lambd = wavelength of laser
    note: default values just to ensure function works
    """
    u = x / (lambd * R)
    C1 = np.pi * A * u
    C2 = np.pi * a * u
    return a**2 * ((np.sin(N * C1) / np.sin(C1)) * (np.sin(C2) / (C2)))**2


if __name__ == '__main__':
    x = np.linspace(-50, 50, 500)*1e-3

    E = illuminance(x=x, lambd=632.8e-9, R=5, A=0.12)
    plt.plot(x, E)
    plt.show()

# Output in terminal
''' 
nick@thinkpad:~/Documents/uio/FYS2150/lab11optikk$ python prelab_nichoka.py 
prelab_nichoka.py:20: RuntimeWarning: invalid value encountered in divide
  return a**2 * ((np.sin(N * C1) / np.sin(C1)) * (np.sin(C2) / (C2)))**2
nick@thinkpad:~/Documents/uio/FYS2150/lab11optikk$ 
'''
# + reasonable looking plot.