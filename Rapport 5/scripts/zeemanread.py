#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Finds diameter of diffraction rings from Zeeman experiment
in the FYS2150 Waveoptics lab
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from scipy import ndimage
# from PIL import Image
# import skimage.morphology as morph
# from skimage import filters


def rgb2gray(rgb):
    '''
    Converts shape=(N,M,rgb) array to (N, M) grayscale array
    '''
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114]).astype(int)


def gray2binary(gray, limBW=128):
    """Converts grayscale image to binary grayscale of 0 OR 255
    image must be array of shape=(N, M)
    gray: (N, M) array
    limBW: threshhold limit between B/W
    """
    bw = np.asarray(gray).copy()
    bw[bw < limBW] = 0      # Black
    bw[bw >= limBW] = 255   # White
    return bw


def readZeeman(filename, lowerThresh, higherThresh, g2bThresh=20):
    #import skimage.color
    if isinstance(filename, basestring) is False:
        raise TypeError("Filename arguement not string")
    img = imread(filename)
    bwImg = rgb2gray(img)
    binImg = gray2binary(bwImg, 17)
    binCrop = binImg[475:525, 0:-1]

    plt.imshow(bwImg, cmap=plt.get_cmap('gray'))
    plt.close()
    plt.axhline(0, linestyle="-", color="r")
    plt.imshow(binCrop, cmap=plt.get_cmap('gray'))
    plt.close()

    edge_horizont = ndimage.sobel(binCrop, 0)
    edge_vertical = ndimage.sobel(binCrop, 1)
    magnitude = np.hypot(edge_horizont, edge_vertical)
    outlines = gray2binary(magnitude, g2bThresh)
    plt.imshow(outlines, cmap=plt.get_cmap("gray"))

    outline_indeces = []

    for i in range(len(outlines)):
        outline_indeces_row = [0]  # Setting first element to zero to make loop work
        for j in range(len(outlines[i])):
            if outlines[i, j] == 0:
                pass
            else:
                if abs(j - outline_indeces_row[-1]) < 4:
                    pass
                else:
                    outline_indeces_row.append(j)
        outline_indeces_row.pop(0)  # remove the zero
        outline_indeces.append(outline_indeces_row)
    d_outlines = outline_indeces[30]

    plt.plot(d_outlines, np.zeros_like(d_outlines) + 30, "ro")
    plt.title("Chose lower and higher threshhold")
    plt.close()

    d_outlines = filter(lambda f: f < higherThresh and f > lowerThresh, d_outlines)

    if len(d_outlines)%2 != 0:
        raise ValueError("outlines not even number, check threshhold")

    d_center = []
    counter = 0
    while counter < len(d_outlines):
            d_center.append((d_outlines[counter] + d_outlines[counter + 1]) / 2.0)
            counter += 2
    plt.imshow(binCrop, cmap=plt.get_cmap("gray"))
    plt.plot(d_center, np.zeros_like(d_center) + 30, "ro")
    plt.yticks([])
    plt.xticks(d_center, rotation=-25)
    plt.close()

    d_3 = d_center[-1] - d_center[0]
    d_2 = d_center[-2] - d_center[1]
    d_1 = d_center[-3] - d_center[2]
    
    return d_1, d_2, d_3 

d14, d24, d34 = readZeeman("figs/ZEEMAN4A.jpg", 255, 955)
d13, d23, d33 = readZeeman("figs/ZEEMAN3A.jpg", 255, 955)
d12, d22, d32 = readZeeman("figs/ZEEMAN2A.jpg", 255, 955)
#readZeeman("figs/ZEEMAN1A.jpg", 255, 955, 100)



def readZeemanAlt(filename):
    #import skimage.color
    if isinstance(filename, basestring) is False:
        raise TypeError("Filename arguement not string")
    img = imread(filename)
    bwImg = rgb2gray(img)
    binImg = gray2binary(bwImg, 17)
    binCrop = binImg[475:525, 0:-1]
    bwCrop = bwImg[475:525, 0:-1]
    bwRow = bwCrop[30]
    plt.imshow(bwImg, cmap=plt.get_cmap('gray'))
    plt.close()
    plt.subplot(212)
    plt.axhline(0, linestyle="-", color="r")
    plt.imshow(bwCrop, cmap=plt.get_cmap('gray'))
    plt.xlabel("Pixel")
    plt.yticks([])
    plt.subplot(211)
    plt.plot(bwRow)
    plt.ylabel("Intensity"); plt.xlabel("Pixel")
    plt.tight_layout()
    plt.close()

readZeemanAlt("figs/ZEEMAN1A.jpg")

def mu_B(B, d1, d2, d3):
    hc = 1.98644568E-25     # [CODATA]
    sigma = float(d2**2 - d1**2) / (d3**2 - d1**2)
    tx4 = 3.0 * 4.0

    return (hc / tx4) * (sigma / B)

mu_B_4 = mu_B(685.5e-3, d14, d24, d34)
mu_B_3 = mu_B(526.5e-3, d13, d23, d33)
mu_B_2 = mu_B(354.5e-3, d12, d22, d32)

def print_diameters(list):
    n = 1
    for item in list:
        print "d_%i = %.1f" % (n, item)
        n += 1
    return

print "\n4A Diameters"
print_diameters([d14, d24, d34])

print "\n3A Diameters"
print_diameters([d13, d23, d33])

print "\n2A Diameters"
print_diameters([d12, d22, d32])

print "\nMu_B:\n"
print "I = 4A -> %.4e" % mu_B_4
print "I = 3A -> %.4e" % mu_B_3
print "I = 2A -> %.4e" % mu_B_2


print "Mean mu_B", np.mean([mu_B_4, mu_B_3, mu_B_2])
