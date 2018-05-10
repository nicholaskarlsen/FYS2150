#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''

import numpy as np
import skvideo.io
import inspect
import os
import matplotlib.pyplot as plt
import scipy.constants
from skimage.measure import regionprops
from matplotlib.image import imread
from skimage import util
# import skimage.color
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
    plt.show()
    plt.axhline(0, linestyle="-", color="r")
    plt.imshow(binCrop,cmap=plt.get_cmap('gray'))
    plt.show()


readZeeman("figs/ZEEMAN4A.jpg")