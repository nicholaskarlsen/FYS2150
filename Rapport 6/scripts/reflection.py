#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by nicholas karlsen

import numpy as np
import matplotlib.pyplot as plt

def read_capfile(filename):
	capfile = open(filename, "r")

	time = []
	angle = []; intensity = []

	for i in range(4):
		capfile.readline()
	for line in capfile:
		col = line.split()
		time.append(col[0])
		intensity.append(col[1])
		angle.append(col[2])
	capfile.close()

	return time, angle, intensity

time1, angle1, intensity1 = read_capfile("data/run1_s_polarisert.txt")

plt.plot(time1, angle1, "x")
plt.show()