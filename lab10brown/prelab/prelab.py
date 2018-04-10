import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

file = Image.open("gitter20x.png")
img = np.array(file)
#pix[pix<= 255*0.8] = 0
#pix[pix>= 255*0.8] = 1

    
mean_im = np.mean(img[:, :])