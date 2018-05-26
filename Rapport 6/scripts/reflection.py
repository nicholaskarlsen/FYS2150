#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nicholas karlsen

import numpy as np
import matplotlib.pyplot as plt


def read_capfile(filename):
    capfile = open(filename, "r")

    time = []
    angle = []
    intensity = []
    capfile.readline()
    # print capfile.readline().split()[:4]
    for i in range(2):
        capfile.readline()
    # Capfile uses decimal "," so replacing with decimal "."
    for line in capfile:
        col = line.split()
        time.append(col[0].replace(",", "."))
        intensity.append(col[1].replace(",", "."))
        angle.append(col[2].replace(",", "."))
    capfile.close()

    angle = np.array(angle, dtype=float)
    intensity = np.array(intensity, dtype=float)
    time = np.array(time, dtype=float)

    return time, angle, intensity


time1, angle1, intensity1 = read_capfile("data/run1_p_polarisert.txt")
startIndex = 150
stopIndex = 600
poly = np.polyfit(np.rad2deg(angle1)[startIndex:stopIndex], intensity1[startIndex:stopIndex], 2)

theta = np.linspace(0, 60, 1e3)


def plot1():
    plt.plot(np.rad2deg(angle1[:-1]), intensity1[:-1], linestyle="--", color="black")
    plt.plot(np.rad2deg(angle1[:-1]), intensity1[:-1], ".", color="red")
    plt.plot(theta, poly[0] * theta**2 + poly[1] * theta + poly[2])
    plt.xlabel("Angle [deg]")
    plt.ylabel("Intensity [%]")
    plt.title("P-Polarized light")
    plt.grid("on")
    plt.show()


plot1()


time2, angle2, intensity2 = read_capfile("data/run1_s_polarisert.txt")
time3, angle3, intensity3 = read_capfile("data/run2_s_polarisert.txt")


def plot2():
    plt.plot(np.rad2deg(angle2), intensity2, "r.", label="Run #1")
    plt.plot(np.rad2deg(angle3), intensity3, "b.", label="Run #2")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Intensity [%]")
    plt.title("S-Polarized light")
    plt.grid("on")
    plt.legend()
    plt.show()
