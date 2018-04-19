#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Reads video file and converts to binary image
resulting in easy data analysis.
author: Nicholas Karlsen

Note: If skvideo.io package is missing, install
"sk-video" using pip
'''

import numpy as np
import skvideo.io
import inspect, os
from PIL import Image
import matplotlib.pyplot as plt
from skimage import io, color
import skimage.morphology as morph
from skimage.measure import label
from skimage.filters import threshold_otsu

# Name of file, relative path.
_file = "B2.avi"

def rgb2gray(rgb):
    '''
    Converts (x, y, rgb) array to grayscale see wiki page:
    https://en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
    for details
    '''
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

""" 
By default, asumes file is in same folder as script.
Edit this section if in different folder, but
note that skvideo requires the FULL path of file,
not just relative.
"""

# Fetching current dir path
folderPath = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe())))
folderPath = "/home/nick/Videos/fys2150drag"
#adds current dir to filename
filename = folderPath + "/" + _file

video = skvideo.io.vread(filename)
totalFrames = len(video)
print video.shape
print "Number of frames:", len(video)

frameStart = 0
frameStop = totalFrames

xPos = np.zeros(frameStop - frameStart) # x-position of CM
yPos = np.zeros(frameStop - frameStart) # y-position of CM

frameCount = frameStart # Counts frames

print video[500].shape
gray = rgb2gray(video[500])
bw = np.asarray(gray).copy()
# Pixel range is 0...255, 256/2 = 128
bw[bw < 128] = 0    # Black
bw[bw >= 128] = 255 # White
plt.imshow(bw, cmap = plt.get_cmap('gray'))
plt.show()

Strel = morph.disk(10)
Strel2 = morph.disk(11)
plt.figure(figsize=(7,7))
plt.subplot(131)
plt.imshow(Strel)
plt.title("2-Pixel Radius Disk Element")
plt.subplot(133)
plt.imshow(Strel2)
plt.title("5-Pixel Radius Disk Element")

def plot_image(data, title):
    """
    This function is used to plot the images used in this example.
    :param data: image file
    :param title: string to use as the plot title
    """
    plt.figure(figsize=(7,7))
    io.imshow(data)
    plt.axis('off')
    plt.title(title)
    plt.show()

BWimg_dil = morph.dilation(bw, Strel)
plot_image(BWimg_dil, "Dilated")

BWimg_close = morph.closing(BWimg_dil,Strel2)
plot_image(BWimg_close, "Closed")

L = label(BWimg_close)
plot_image(color.label2rgb(L), 'Labeled Regions')

half_length = int(np.floor(np.size(L,1)/2))
L_cntr = L[half_length,half_length]
print "Label of blob that contains the center pixel: {}".format(L_cntr)


Seg = L
Seg[Seg != L_cntr] = 0
Seg[Seg == L_cntr] = 1
plot_image(Seg, 'ROI')


Mask = morph.dilation(Seg,Strel2)
plot_image(Mask, "Mask")

