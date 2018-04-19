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

'skvideo requires full path of video'
'Fetches path of this script'
path = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe())))
'uncomment next line to use other path'
# path = "your path here"
filename = path + "litenmetallkule.avi"

"""
video = skvideo.io.vreader(filename)
#video = cv2.VideoCapture(filename)
for frame in video:
    print frame.shape
"""
