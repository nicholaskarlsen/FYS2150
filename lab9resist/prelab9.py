import numpy as np
import matplotlib.pyplot as plt
import FYS2150lib as fy
from PIL import Image

def ex_4():
    # Ex 4
    Fg = []
    vt_2 = []
    vt_3 = []
    vt_4= []
    file = open('terminal_hastighet.dat', 'r')
    for line in file:
        cols = line.split()
        Fg.append( float(cols[0]) )
        vt_2.append( float(cols[1]) )
        vt_3.append( float(cols[2]) )
        vt_4.append( float(cols[3]) )
    file.close()

    plt.plot(Fg, vt_2, label="vt_2")
    plt.plot(Fg, vt_3, label="vt_3")
    plt.plot(Fg, vt_4, label="vt_4")
    plt.legend()
    plt.show()

    v_fd = vt_3 / np.sqrt(Fg)
    v_fd_std = fy.stddev(v_fd)
    v_fd_mean = np.mean(v_fd)
    print v_fd_std
    print v_fd_mean
ex_4()
def ex_8():
    img = Image.open("ballongbilde.png")
    pix = np.array(img)
    pix[pix<= 255*0.8] = 0
    pix[pix>= 255*0.8] = 1

    img2 = Image.open("areal.png")
    pix2 = np.array(img2)
    
    print pix2[0, 0, 0]
ex_8()
