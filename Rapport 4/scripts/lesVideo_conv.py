#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Reads video file and converts to binary image
resulting in easy data analysis.
author: Nicholas Karlsen

Note: skvideo is not included in anaconda by default,
install by 'pip install sk-video' in terminal.
'''

import numpy as np
import skvideo.io
import inspect
import os
import matplotlib.pyplot as plt
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


def trackCircle(filename="litenmetallkule.avi", path="current",
                hMin=0, hMax=-1, wMin=0, wMax=-1):
    """
    Takes video file as input, filters out static background based on
    first frame and finds the CM of circle in every frame. Requires
    circle to be only object in frame (after filtering), so requires static
    background. If not, try adjust hMin, hMax, wMin, wMax to crop out moving
    background.
    filename: filename of video
    path: FULL path of file, eg '/home/nick/Videos/fys2150drag'.
          if left as default, it will asume same path as script.
    hMin, hMax, wMin, wMax: used for cropping the image.
    """
    # Fetching current dir path
    folderPath = os.path.dirname(
        os.path.abspath(
            inspect.getfile(
                inspect.currentframe())))
    if path != "current":
        folderPath = path
        "if path is specified"

    # skvideo requires full path
    fullFilename = folderPath + "/" + filename

    print "Reading video..."

    video = skvideo.io.vread(fullFilename)
    totalFrames = len(video)

    print "Number of frames:", len(video)

    frameStart = 0
    frameStop = totalFrames

    "Creates array to store x, y vals of CM"
    cmPos = np.zeros([frameStop - frameStart, 2])

    validFrames = []  # Keeps track of usable frames

    def genFilter(image):
        """
        Generates an array to filter out
        static background based on first frame

        NOT YET IMPLEMENTED
        """
        gsImage = rgb2gray(image)
        bwImage = gray2binary(gsImage)
        bwImage = bwImage / 255.0
        return bwImage.astype(int)

    def detectCirc(image):
        """
        Inverts color of image and detects center of circle shape.
        Asumes circle is the ONLY object in image, so noise
        needs to be filtered out
        """
        #staticBg = genFilter(video[0])

        invFrame = image
        bwFrame = gray2binary(
            rgb2gray(
                util.invert(invFrame)))[hMin:hMax, wMin:wMax]
        bwFrame = bwFrame  # * staticBg
        # Detects shapes in image
        props = regionprops(label_image=bwFrame.astype(int))

        return props, invFrame, bwFrame

    for frame in xrange(totalFrames):
        """
        Need to invert image for regionprops to work, only finds white obj
        on black background, not black on white.
        """
        # convert to binary grayscale to filter out noise
        props = detectCirc(video[frame])[0]

        # Bad way of checking if the ball is in frame
        if len(props) == 0:
            pass
        else:
            cmPos[frame] = props[0].centroid  # Detects centroids
            validFrames.append(frame)  # Keeps track of frames with ball

            # Print info to terminal while processing
            print "frame", frame,\
                  "-", "Center of mass:",\
                  "x=%i, y=%i" % (cmPos[frame][1], cmPos[frame][0])

    def plot_im(frame=int(totalFrames / 2.0)):
        "plot frame + CM, used to check functionality"
        im = video[frame]
        props, invFrame, bwFrame = detectCirc(im)
        cmPos[frame] = props[0].centroid
        plt.subplot(311)
        plt.imshow(invFrame)
        plt.title("Raw image, frame:%i" % frame)
        plt.plot(cmPos[frame, 1], cmPos[frame, 0] + hMin,
                 "ro", label="Center of mass")
        plt.legend()
        plt.subplot(312)
        plt.imshow(bwFrame, cmap=plt.get_cmap('gray'))
        plt.plot(cmPos[frame, 1], cmPos[frame, 0],
                 "ro", label="Center of mass")
        plt.title("Processed image, frame:%i" % frame)
        plt.legend()
        plt.show()
    plot_im()

    return cmPos.astype(int), validFrames


def testFunc():
    """
    Testing that method of finding C.M works properly
    """
    import skimage.color
    #img = imread("bilde5.png")
    img = imread("frame_inv2.png")
    bwImg = skimage.color.rgb2gray(img)
    plt.subplot(211)
    plt.imshow(bwImg, cmap=plt.get_cmap('gray'))

    props = regionprops(label_image=bwImg.astype(int))
    cm = props[0].centroid

    plt.subplot(212)
    plt.imshow(img)
    plt.plot(cm[1], cm[0], "ro",
             label="Center of mass = (%i, %i)" % (cm[1], cm[0]))
    plt.legend()
    plt.show()


if __name__ == "__main__":

    folderPath = "/home/nick/Videos/fys2150drag"

    cm, validFrames = trackCircle(filename="B2.avi",
                                  path=folderPath,
                                  hMin=67, hMax=216)

    if len(cm[:, 1]) != len(validFrames):
        print "Tracking interupted in some frames,"
        print "Only returning uninterupted frames."
        x = []
        y = []
        for validFrame in validFrames:
            x.append(cm[validFrame, 1])
            y.append(cm[validFrame, 0])
        x = np.array(x).astype(int)
        y = np.array(y).astype(int)
    else:
        x = cm[validFrames[0]:validFrames[-1], 1]
        y = cm[validFrames[0]:validFrames[-1], 0]

    plt.subplot(211)
    plt.plot(validFrames, x, "x")
    plt.xlabel("Frame")
    plt.ylabel("x-position of center of mass [px]")
    plt.subplot(212)
    plt.plot(validFrames, y, "x")
    plt.xlabel("Frame")
    plt.ylabel("y-position of center of mass [px]")
    plt.show()
