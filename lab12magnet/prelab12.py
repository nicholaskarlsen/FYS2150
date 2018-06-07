#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Prelab for FYS2150: Magnetism
"""

import numpy as np

# ..._par -> parallel
# ..._tan -> tangential


def f(a_par, a_tan):
    return float(a_par) / a_tan


def epsilon(f):
    return np.sqrt(1 - (1.0 / f**2))


def D_par(f):
    if epsilon(f) == 0:
        return 1.0 / 3.0
    else:
        P1 = 1 - (1.0 / epsilon(f)**2)
        P2 = 1 - 1.0 / (2.0 * epsilon(f)) *\
            np.log((1 + epsilon(f)) / (1 - epsilon(f)))

        return P1 * P2


def D_tan(f):
    if D_par(f) == 1:
        return 0
    else:
        return (1 - D_par(f)) / 2.0

# Run example in terminal
# Doesnt seem to work properly for f < 1
"""
nick@thinkpad:~/Documents/uio/FYS2150/lab12magnet$ python
Python 2.7.14 |Anaconda custom (64-bit)| (default, Dec  7 2017, 17:05:42) 
[GCC 7.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from prelab12 import *
>>> D_par(1)
0.3333333333333333
>>> D_tan(1)
0.33333333333333337
>>> D_par(1.75)
0.1997871217870338
>>> D_tan(1.75)
0.4001064391064831
>>> D_par(0.000000000001)
prelab12.py:18: RuntimeWarning: invalid value encountered in sqrt
  return np.sqrt(1 - (1.0 / f**2))
nan
>>> D_par(1e-4)
nan
>>> D_par(1e-2
... )
nan
>>> D_par(0.1)
nan
>>> D_par(0.9)
nan
>>> D_par(1)
0.3333333333333333
>>> D_par(0.999999)
nan
>>> 
"""