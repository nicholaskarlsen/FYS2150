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
import inspect
import os
from PIL import Image
import matplotlib.pyplot as plt
from skimage.measure import regionprops
import skimage.morphology as morph
from skimage import filters


_file = "B2.avi"

def rgb2gray(rgb):
    '''
    Converts shape=(x,y,rgb) array to grayscale see wiki page:
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

print "Reading video..."

video = skvideo.io.vread(filename)
totalFrames = len(video)
print video.shape
print "Number of frames:", len(video)

frameStart = 0
frameStop = totalFrames
frameCount = frameStart     # Counts frames

"Creates array to store x, y vals of CM"
xPos = np.zeros(frameStop - frameStart)     # x-position of CM
yPos = np.zeros(frameStop - frameStart)     # y-position of CM

for frame in xrange(600, 601):
    gray = rgb2gray(video[frame])
    bw = np.asarray(gray).copy()
    limBW = 128             # Threshhold of B/W
    bw[bw < limBW] = 0      # Black
    bw[bw >= limBW] = 255   # White
    bw = bw.astype(int)     # Setting type to integer, for regionprops to work
    props = regionprops(label_image=bw)     # Detects shapes in image
    cm = props[0].centroid                  # Detects centroids
    xPos[frameCount] = cm[0]                # save xpos of centroid
    yPos[frameCount] = cm[1]                # save ypos of centroid
    print "frame", frameCount, "-", "Center of mass:", cm
    frameCount += 1

    def plot_im():
        "plot frame + CM, used to check functionality"
        fig = plt.figure()
        plt.subplot(211)
        plt.imshow(video[frame])
        plt.subplot(212)
        plt.imshow(bw, cmap = plt.get_cmap('gray'))
        plt.plot(cm[1], cm[0], "ro", label="Center of mass")
        plt.legend()
        plt.show()
    plot_im()




"""
fig2 = plt.figure()
plt.subplot(221)
plt.plot(xPos, "x")
plt.subplot(212)
plt.plot(yPos, "x")
plt.show()
"""
"""
for frame in range(totalFrames):
    image = rgb2gray(video[frame])
    threshold_value = filters.threshold_otsu(image)
    labeled_foreground = (image > threshold_value).astype(int)
    properties = regionprops(labeled_foreground, image)
    center_of_mass = properties[0].centroid
    weighted_center_of_mass = properties[0].weighted_centroid

    print(center_of_mass)
"""