import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat("Vbro.mat")
Vbro = data.get("Vbro")

print Vbro
plt.plot(Vbro[::1000])
plt.show()

fourier = np.fft.fft(Vbro)
