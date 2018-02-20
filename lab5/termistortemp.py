import matplotlib.pyplot as plt
import numpy as np
"""
import scipy.io as sio
import numpy as np

data = sio.loadmat("linjedata.mat")

x = data.get("x")
"""

def Temp(R):
    return 1.0 / a + b*np.log(R) + c*(np.log(R))**3