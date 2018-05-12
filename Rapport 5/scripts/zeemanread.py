#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from skimage import measure
from scipy import ndimage
# from PIL import Image
# import skimage.morphology as morph
# from skimage import filters


def rgb2gray(rgb):
    '''
    Converts shape=(N,M,rgb) array to (N, M) grayscale array see wiki page
    '''
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114]).astype(int)


def gray2binary(gray, limBW=128):
    """Converts grayscale image to binary grayscale of 0 OR 255
    image must be array of shape=(N, M)
    gray: (N, M) array
    limBW:
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
    plt.imshow(binCrop,cmap=plt.get_cmap('gray'))
    plt.close()

    edge_horizont = ndimage.sobel(binCrop, 0)
    edge_vertical = ndimage.sobel(binCrop, 1)
    magnitude = np.hypot(edge_horizont, edge_vertical)

    plt.imshow(magnitude, cmap=plt.get_cmap("gray"))
    plt.show()
readZeeman("figs/ZEEMAN4A.jpg")