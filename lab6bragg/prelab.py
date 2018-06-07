import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
import FYS2150lib as fys

def misc():
    e = 1.602e-19
    h = 6.626e-34
    c = 299792458
    E = e * 20e3


    lambd = h * c / E

    print "(ex4) lambda = ", lambd

    omega_2 = range(12, 26)
    d_2 = 401e-12
    intensity = [130, 124, 133, 131, 128, 132, 138,
                 192, 244, 301, 348, 403, 462, 508]
    lamb_2 = d_2 * np.sin(np.deg2rad(omega_2))

    plt.plot(omega_2, intensity, "x")
    plt.close()

    wavelen = d_2 * np.sin(np.deg2rad(18.0 / 2.0))

    Energy = const.h * const.c / (wavelen * const.e)

    print const.e
    print "HERE",Energy / 1e3
misc()


def f(U, m=const.m_e):
    K1 = const.e / (2 * m * const.c**2)
    return 1.0 / np.sqrt(1 + K1 * U)


print f(8e3)


def ex8():
    col1 = []
    col2 = []
    file = open('diameter.dat', 'r')
    for line in file:
        cols = line.split()
        col1.append(float(cols[0]))
        col2.append(float(cols[1]))
    file.close()

    U = np.array(col1)
    D = np.array(col2)
    lambd_C = const.physical_constants["Compton wavelength"][0]

    lambd = lambd_C * np.sqrt(const.m_e * const.c**2 / (2 * const.e * U)) * f(U)

    phi_bar = 1.0 / len(lambd) * np.sum(lambd / D)
    print phi_bar
    print fys.stddev(lambd / D)

ex8()
