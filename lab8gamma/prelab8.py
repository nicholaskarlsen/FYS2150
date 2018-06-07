import scipy.io as sio
import numpy as np
import FYS2150lib

data = sio.loadmat("poisson.mat")
dat = data.get("data")

print np.std(dat)
print np.mean(dat)


skjerming = np.array([
				0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0
				]) * 1e-3

n = np.array([
			13.7, 12.4, 11.0, 9.7, 8.9, 7.9, 7.1
			])

mu = (np.log(n[0]) - np.log(n)) / skjerming

dm, dc, c, m = FYS2150lib.linfit(skjerming, np.log(n))
print "\nex5:"
print m, dm
print c, dc

print "\nex 4:"

r = 2e-2
d = 20e-2
A = 10e6
nr = 23
nb = 2

omega = r**2 * np.pi / d**2
omega_red = omega / (np.pi * 4.0)


eff = float(nr - nb) / (A * omega_red)

print "\nex9:"
I = np.array([410, 773])
E = np.array([662, 1275])

s = float(E[1] - E[0]) / (I[1] - I[0])
print s

print E[1] - s*I[1]
print E[0] - s*I[0]