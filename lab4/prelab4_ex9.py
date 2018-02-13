import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat("Vbro.mat")
Vbro = data.get("Vbro")

print Vbro

fourier = np.fft.fft(Vbro)