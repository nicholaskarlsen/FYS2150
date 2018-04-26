#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Reads video file and converts to binary image
resulting in easy data analysis.
author: Nicholas Karlsen

Note: skvideo is not included in anaconda python,
install by 'pip install sk-video' in terminal.
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
import FYS2150lib as fys # Used for linfit
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

def genFilter(image):
    """
    Generates an array to filter out
    static background based on first frame
    """
    gsImage = rgb2gray(image)
    bwImage = gray2binary(gsImage)
    bwImage = bwImage / 255.0
    return bwImage.astype(int)

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

    # If path is specified, use that instead.
    if path != "current":
        folderPath = path
        "if path is specified"

    fullFilename = folderPath + "/" + filename

    print "Reading video... %s" %fullFilename

    video = skvideo.io.vread(fullFilename)
    totalFrames = len(video)

    print "Number of frames:", len(video)

    frameStart = 0
    frameStop = totalFrames

    "Creates array to store x, y vals of CM"
    cmPos = np.zeros([frameStop - frameStart, 2])

    validFrames = []  # Keeps track of usable frames

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
            cmPos[frame] = "nan"
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
        plt.savefig("figs/graphs/%s_1.png"%vids[row][:-4])
        plt.legend()
        plt.subplot(313)
        plt.hist(np.ravel(im), 256)
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

    def readlabdat(filename):
        """
        Used to read the file which stores the parameters of the
        sphere
        """
        vids = []; mass = []; radius = []; temp = []
        
        file = open(filename, "r")
        for line in file:
            cols = line.split()
            mass.append(cols[1])
            radius.append(cols[2])
            temp.append(cols[-2])
            vids.append(cols[-1])
        file.close()

        return mass, radius, temp, vids
    mass, radius, temp, vids = readlabdat("data/labdata.dat")

    folderPath = "/home/nick/Videos/fys2150drag"

    rows = [7, 8, 9, 10]

    outfile = open("data/B_results.dat", "w")

    for row in rows:
        cm, validFrames = trackCircle(filename=str(vids[row]),
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

        x = np.array(x)
        y = np.array(y)
        validFrames = np.array(validFrames)

        print "Find start/stop of terminal velocity (straight, steep line) to perform linfit:"
        plt.subplot(211)
        plt.plot(validFrames, x, "o")
        plt.xlabel("Frame")
        plt.ylabel("x-position of center of mass [px]")
        plt.title("Use to determine start/stop frame of linfit")
        plt.subplot(212)
        plt.plot(np.diff(x))
        plt.show()

        start = int(input("Start index:"))
        stop = int(input("Stop index:"))

        m, c, dm, dc = fys.linfit(validFrames[start:stop], x[start:stop])

        plt.subplot(211)
        plt.plot(validFrames, x, ".", label="Position of CM")
        plt.plot(validFrames[start:stop],
                 validFrames[start:stop] * m + c,
                 label="linear fit, y=mx+c")
        plt.text(0, 1000, "m = %i [px/frame]\n dm = %i [px/frame]" % (m, dm))
        plt.xlabel("Frame")
        plt.ylabel("x-pos [px]")
        plt.legend()
        plt.subplot(212)
        plt.plot(validFrames, y, ".", label="Position of CM")
        plt.xlabel("Frame")
        plt.ylabel("y-pos  [px]")
        plt.savefig("figs/graphs/%s_2.png"%vids[row][:-4])
        plt.show()

        outfile.write(vids[row] + " & " + "%i"%(m) + " & " + "%i"%dm + "&" + "%s"%mass[row] + "&" + "%s"%radius[row] +"\\\ \n")

        # More plots

    outfile.close()