#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Contains light intensity for different setups of polarization filters
# by nicholas karlsen

import numpy as np
import matplotlib.pyplot as plt
import FYS2150lib as fys

angles = np.array([0,
                   -10, -20, -30, -40, -50, -60, -70, -80, -90,
                   10, 20, 30, 40, 50, 60, 70, 80, 90
                   ])

# I - Analysator - Source
lux1 = np.array([705,
                 701, 706, 718, 726, 734, 743, 751, 756, 759,
                 703, 713, 719, 726, 736, 745, 753, 758, 754
                 ])

# I - Analysator - Polarisator - Source
lux2 = np.array([133,
                 129, 119, 103, 82, 59, 38, 20, 8, 4,
                 129, 117, 99, 78, 56, 34, 17, 7, 4
                 ])

# I - pol(-90) - Ana - pol(0) - source
lux3 = np.array([3,
                 4, 8, 13, 16, 16, 13, 9, 5, 3,
                 5, 9, 14, 16, 16, 13, 8, 4, 3
                 ])

plt.plot(angles, lux1, "x")
plt.xlabel("Angle [deg]")
plt.ylabel("intensity [lux]")
plt.title("Measured intensity of light passed through an analyzer")
plt.close()


def write_table(x, y, filename):
    # writes a table in LaTeX format
    if len(x) != len(y):
        raise ValueError("Length of arrays do not match")

    outfile = open("%s.dat" % filename, "w")  # Open file in write mode
    for i in range(len(x)):
        outfile.write("%d" % x[i])
        outfile.write(" & ")
        outfile.write("%d" % y[i])
        outfile.write(" \\\\ \n")
    outfile.close()


write_table(angles, lux1, "data/ana")

# print "Standard deviation of lux1 = %d" % np.std(lux1)


# plt.plot(angles, lux1, "x")

# ex1 plot

def ex1():
    plt.figure(figsize=(3.5, 3.5), dpi=100)
    plt.plot(angles, lux1, "x")

    plt.title("Intensity of light passed\n through a single polarization filter")
    plt.xlabel("Angle of analyzer [deg]")
    plt.ylabel("Intensity [Lux]")

    plt.tight_layout()
    plt.savefig("polartest.png", dpi=150)
    plt.close()


# exercise 2 plot`
def ex2():

    angles_rad = np.deg2rad(angles)
    plt.figure(figsize=(3.5, 3.5), dpi=100)

    plt.plot(np.cos(angles_rad) ** 2, lux2 -
             lux2[-1], "x", label="Measured Data")
    x = np.linspace(np.cos(angles_rad[0]) **
                    2, np.cos(angles_rad[-1]) ** 2, 1e3)
    m, c, dm, dc = fys.linfit(np.cos(angles_rad)**2, lux2 - lux2[-1])
    plt.plot(x, m * x + c, label="Linear fit")

    plt.text(0.5, 20, r'$\delta m = %.2e$' % (dm),
             fontsize=10)
    plt.text(0.5, 10, r'$\delta c = %.2e$' % (dc),
             fontsize=10)

    plt.title(
        "Intensity of polarized light\n passed through analyzer for\n different angles $\\theta$")
    plt.xlabel("$\cos^2 \\theta$")
    plt.ylabel("$E(\\theta) - E(\\theta=90^\circ)$ [Lux]")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.savefig("malus1.png", dpi=150)
    plt.close()

    return

def ex3():
    plt.figure(figsize=(3.5, 3.5), dpi=100)
    plt.plot(angles, lux3, "x")
    plt.title("Intensity of light when varying \nangle $\\theta$ of analyzer between \ntwo tangential polarizers")
    plt.xlabel("Angle of analyzer [deg]")
    plt.ylabel("Intensity [Lux]")
    plt.tight_layout()
    plt.savefig("malus2.png", dpi=150)
    plt.show()


if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
