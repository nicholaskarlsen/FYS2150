import numpy as np
import matplotlib.pyplot as plt


e = 1.602e-19
h = 6.626e-34
c = 299792458
E = e * 20e3


lambd = h * c / E

print "(ex4) lambda = ", lambd

omega_2 =  range(12, 26)
d_2 = 401e-12
intensity = [130, 124, 133, 131, 128, 132, 138, 192, 244, 301, 348, 403, 462, 508]
lamb_2 = d_2 * np.sin(np.deg2rad(omega_2))

plt.plot(lamb_2, intensity, "x")
plt.show()

print d_2 * np.sin(np.deg2rad(20)) 