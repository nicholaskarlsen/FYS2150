import numpy as np
import matplotlib.pyplot as plt
import  FYS2150lib
from tabulate import tabulate
import sys
import scipy.io as sio

g = 9.80665  # standard gravity

def import_matlab(filename):
    data = sio.loadmat(filename)
    fw = data.get("fw")
    tw = data.get("tw")

    return fw, tw

L_a_hultafors = np.array([
    119.5, 119.5, 119.45, 119.4, 119.43, 119.4, 119.4, 119.45, 119.4,
    119.43
    ])

L_b_hultafors = np.array([
    119.6, 119.7, 119.6, 119.5, 119.55, 119.6, 119.5, 119.65, 119.6,
    119.55
    ])

L_a_laser = np.array([
    120.5, 119.6, 119.5, 119.4, 119.4, 119.68, 119.9, 130.6, 119.4,
    0
    ])

L_b_laser = np.array([
    120.6, 119.8, 119.7, 119.6, 119.6, 119.72, 119.7, 130.2, 119.5,
    0
    ])

pendel_period = np.array([
    7.30, 7.72, 7.57 , 7.43, 7.73, 7.27, 7.68, 7.60, 7.34, 7.75,
    7.06, 7.32, 7.55, 7.29, 7.08, 7.82, 7.78, 7.44, 7.68, 7.46
    ])


def rc_data():
    fw, tw = import_matlab("labdata/rc_1.mat")
    print fw[:, 2:8]
    plt.plot(tw[:, 2:8], fw[:, 2:8], "o", color="blue")
    plt.show()

    v = FYS2150lib.vel(fw, 1.286e4)
    plt.plot(tw[:, 2:8], v[:, 2:8], "x", color="blue")

    dm, dc, c, m = FYS2150lib.linfit(tw[:, 2:8], v[:, 2:8])
   # v_fit = m*tw[:, 2:8] + c
    v_fit = np.polyfit(np.transpose(tw[:, 2:8]), np.transpose(v[:, 2:8]), 1)
    plt.plot(tw[:, 2:8], v_fit, linestyle="--")
    plt.show()

rc_data()



if __name__ == '__main__':

    def tab():
        lendat = np.zeros([len(L_a_hultafors), 4])
        lendat[:, 0] = np.transpose(L_a_hultafors)
        lendat[:, 1] = np.transpose(L_b_hultafors)
        lendat[:, 2] = np.transpose(L_a_laser)
        lendat[:, 3] = np.transpose(L_b_laser)
        #L_ab_hultafors = abs(L_b_hultafors - L_a_hultafors)
        #L_ab_laser = abs(L_b_laser - L_a_laser)
        
        sys.stdout = open("tables/lendat.tex", "w")   # prints output to file instead of terminal.
        print(tabulate(lendat ,headers=["Ruler, a [cm]", "Ruler, b [cm]", "Laser, a [cm]", "Laser, b [cm]"], tablefmt="latex", floatfmt=".2f"))
        sys.stdout.close()

    print np.mean(pendel_period)

    """
    diff_hultfors = abs(L_a_hultafors - L_b_hultafors)
    diff_laser = abs(L_a_laser - L_b_laser)

    print np.mean(diff_hultfors), np.mean(diff_laser)
    print error_mean(abs(L_a_hultafors - L_b_hultafors))
    print error_mean(abs(L_a_laser - L_b_laser))

    """