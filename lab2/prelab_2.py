import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat("RC_data.mat")
frekvens = data.get("frekvens")
Vu_over_Vi = data.get("Vu_over_Vi")

print frekvens
