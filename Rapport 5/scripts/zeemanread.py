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


def readZeeman(filename):
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
    outlines = gray2binary(magnitude, 20)
    plt.imshow(outlines, cmap=plt.get_cmap("gray"))
    print np.shape(outlines)

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
    print outline_indeces[30]
    plt.plot(outline_indeces[30], np.zeros_like(outline_indeces[30]) + 30, "rx")
    plt.show()


readZeeman("figs/ZEEMAN4A.jpg")