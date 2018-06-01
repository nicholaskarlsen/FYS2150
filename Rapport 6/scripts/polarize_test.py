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
plt.title("Measured intensity of light passed through an analyzator")
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


#plt.plot(angles, lux1, "x")

# exercise 2 plot
def ex2():

    angles_rad = np.deg2rad(angles)
    plt.plot((lux2 - lux2[-1]), np.cos(angles_rad)
             ** 2, "x", label="Measured Data")
    x = np.linspace(lux2[0] - lux2[-1], 0, 1e3)
    m, c, dm, dc = fys.linfit(lux2 - lux2[-1], np.cos(angles_rad)**2)
    plt.plot(x, m * x + c, label="Linear fit")
    plt.legend()
    plt.show()

    return


if __name__ == '__main__':
    ex2()
