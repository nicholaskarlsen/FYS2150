import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.constants as const
"""
file = Image.open("gitter20x.png")
img = np.array(file)
#pix[pix<= 255*0.8] = 0
#pix[pix>= 255*0.8] = 1

    
mean_im = np.mean(img[:, :])
"""

mu = 1e-3
FPS = 15.0
sx = 0.23e-6
D = 8 
T = 20 + 273.25
val = 1.4

k = FPS * sx**3 * 3.0 * np.pi * mu * D / (4.0 * T) * val

# d(<xx + yy>)/dt burde gaa mot; (i 20C)
print const.k / (FPS * sx**3 * 3.0 * np.pi * mu * D / (4.0 * T))



print const.k

print k