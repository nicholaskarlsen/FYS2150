import numpy as np
import matplotlib.pyplot as plt
import  FYS2150lib
from tabulate import tabulate
import sys
import scipy.io as sio
from collections import OrderedDict

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

L_a_hultafors_err = np.array([
    0.23, 0, 0.37, 0, 0.4, 0.2, 0.27, 0.35, 0.39, 0.31
    ])

L_b_hultafors = np.array([
    119.6, 119.7, 119.6, 119.5, 119.55, 119.6, 119.5, 119.65, 119.6,
    119.55
    ])

L_b_hultafors_err = np.array([
    0.23, 0, 0.37, 0, 0.4, 0.2, 0.27, 0.35, 0.39, 0.31
    ])

L_a_laser = np.array([
    120.5, 119.6, 119.5, 119.4, 119.4, 119.68, 119.9, 130.6, 119.4
    ])

L_a_laser_err = np.array([
    0.2, 0.205, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.22, 0
    ])

L_b_laser = np.array([
    120.6, 119.8, 119.7, 119.6, 119.6, 119.72, 119.7, 130.2, 119.5
    ])

L_b_laser_err = np.array([
    0.2, 0.205, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.22, 0
    ])

L_ab_direct = np.array([
    1.25, 1.40, 1.20, 1.80, 1.80, 1.50
    ])


pendel_period = np.array([
    7.30, 7.72, 7.57 , 7.43, 7.73, 7.27, 7.68, 7.60, 7.34, 7.75,
    7.06, 7.32, 7.55, 7.29, 7.08, 7.82, 7.78, 7.44, 7.68, 7.46
    ])

legobil_freq = 7718     # Hz 
rc_freq = 1.286e4       # Hz

def rc_data(a, b, filename, f, title, figname):
    fw, tw = import_matlab(filename)
    plt.plot(tw[:, a:b], fw[:, a:b], "o", color="blue")
    plt.close()

    t_err = np.transpose(tw[:, 1]) - np.transpose(tw[:, 0])

    v = FYS2150lib.vel(fw, f)

    dm, dc, c, m = FYS2150lib.linfit(tw[:, a:b], v[:, a:b])
    v_fit = m*tw[:, a:b] + c

    plt.plot(tw[:, a:b], v[:, a:b], "x", color="red", label="Data Points")
    plt.errorbar(np.transpose(tw[:, a:b]), np.transpose(v_fit), yerr=dm, color="blue", fmt='o', label="Error Range")
    plt.plot(np.transpose(tw[:, a:b]), np.transpose(v_fit), linestyle="-", color="black", label="Linear Fit")

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.ylabel("Velocity $[ms^{-1}]$")
    plt.xlabel("Time [s]")
    plt.title("%s \n a=%.2f, $\delta a$ =%.2f$ms^{-1}$" % (title, m, dm))
    plt.savefig("figs/%s.png"%figname)
    plt.close()

    #print title, dm, dc, c, m

rc_data(2, 7, "labdata/legobilh_16cm.mat", legobil_freq, "Lego car, h=16cm", "lego16cm")

rc_data(4, 8, "labdata/legobil1h_27cm.mat", legobil_freq, "Lego car, h=27cm", "lego27cm")

rc_data(9, 14, "labdata/lrgebilh_37cm.mat", legobil_freq, "Lego car, h=37cm", "lego37cm1")
rc_data(37, 42, "labdata/lrgebilh_37cm.mat", legobil_freq, "Lego car, h=37cm", "lego37cm2")
rc_data(60, 65, "labdata/lrgebilh_37cm.mat", legobil_freq, "Lego car, h=37cm", "lego37cm3")

def rc_vel(a, b, filename, f, title, figname):
    fw, tw = import_matlab(filename)
    plt.plot(tw[:, a:b], fw[:, a:b], "o", color="blue")
    plt.close()

    v = FYS2150lib.vel(fw, f)
    v_abs = np.sqrt(v**2)
    plt.plot(tw[:, a:b], v_abs[:, a:b], "x", color="red")
    plt.ylabel("|v| $[ms^{-1}]$")
    plt.xlabel("Time [s]")
    plt.ylim(0, 4)
    plt.xlim(0, 7)
    plt.title("%s" % (title))
    plt.savefig("figs/%s.png"%figname)
    plt.close()
rc_vel(0, -1, "labdata/RC_3.mat", rc_freq, "RC-car, attempt 3", "RC_3abs")
rc_vel(0, -1, "labdata/RC_2.mat", rc_freq, "RC-car, attempt 2", "RC_2abs")
rc_vel(0, -1, "labdata/rc_1.mat", rc_freq, "RC-car, attempt 1", "RC_1abs")


def freq_dat(a, b, filename, f, title, figname):
    fw, tw = import_matlab(filename)
    plt.plot(tw[:, a:b], fw[:, a:b], "x", color="blue")
    plt.ylabel("$f_m$ [Hz]")
    plt.xlabel("Time [s]")
    plt.ylim(f - 100, f+100)
    plt.xlim(0, 7)
    plt.title("%s" % (title))
    plt.savefig("figs/%s.png"%figname)
    plt.close()
#freq_dat(0, -1, "labdata/legobilh_16cm.mat", legobil_freq, "Lego car, h=16cm", "lego16cm_freq")
#freq_dat(0, -1, "labdata/legobil1h_27cm.mat", legobil_freq, "Lego car, h=27cm", "lego27cm_freq")
#freq_dat(0, -1, "labdata/lrgebilh_37cm.mat", legobil_freq, "Lego car, h=37cm", "lego37cm_freq")

freq_dat(0, -1, "labdata/RC_3.mat", rc_freq, "RC-car, attempt 3", "RC_3freq")
freq_dat(0, -1, "labdata/RC_2.mat", rc_freq, "RC-car, attempt 2", "RC_2freq")
freq_dat(0, -1, "labdata/rc_1.mat", rc_freq, "RC-car, attempt 1", "RC_1freq")



def histogram1():
    sig = FYS2150lib.stddev(pendel_period)[0]
    sig_m = FYS2150lib.stddev(pendel_period)[1]
    mean = np.mean(pendel_period)
    plt.hist(pendel_period, bins=10, rwidth=1, color="blue")
    plt.xlabel("T [s]")
    plt.ylabel("N")
    plt.title("Measurements of Period of Foucault's Pendulum\n$T_{mean}$=%.2fs, $\sigma=$%.2f,$\sigma_m=$%.2f"%(mean, sig, sig_m))
    plt.axvline(mean, linestyle="--", color="red")
    plt.savefig("figs/period.png")
    plt.close()
histogram1()



def errors_len():
    print
    print "Ruler data:"
    print "mean l_a", np.mean(L_a_hultafors)
    print "std l_a", FYS2150lib.stddev(L_a_hultafors)[0]
    print "std mean l_a", FYS2150lib.stddev(L_a_hultafors)[1]

    print "mean l_b", np.mean(L_b_hultafors)
    print "std l_b", FYS2150lib.stddev(L_b_hultafors)[0]
    print "std mean l_b", FYS2150lib.stddev(L_b_hultafors)[1]
    diff_hultfors = abs(L_a_hultafors - L_b_hultafors)
    print "mean diff", np.mean(diff_hultfors)
    print "std diff", FYS2150lib.stddev(diff_hultfors)[0]
    print "std mean diff", FYS2150lib.stddev(diff_hultfors)[1]

    print "\n -----------\n"
    print "Laser data:"
    print "mean l_a", np.mean(L_a_laser)
    print "std l_a", FYS2150lib.stddev(L_a_laser)[0]
    print "std mean l_a", FYS2150lib.stddev(L_a_laser)[1]

    print "mean l_b", np.mean(L_b_laser)
    print "std l_b", FYS2150lib.stddev(L_b_laser)[0]
    print "std mean l_b", FYS2150lib.stddev(L_b_laser)[1]
    diff_laser = abs(L_a_laser - L_b_laser)
    print "mean diff", np.mean(diff_laser)
    print "std diff", FYS2150lib.stddev(diff_laser)[0]
    print "std mean diff", FYS2150lib.stddev(diff_laser)[1]
errors_len()

print FYS2150lib.stddev(np.array([2.29, 2.29, 1.99]))

print "\nVernier:"
print "mean:", np.mean(L_ab_direct*1e-1)
print "sigma, sigma_m", FYS2150lib.stddev(L_ab_direct*1e-1)