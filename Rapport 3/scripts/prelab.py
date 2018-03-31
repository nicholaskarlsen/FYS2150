import numpy as np
import matplotlib.pyplot as plt
import FYS2150lib

# Ex 4
m = []
h = []
file = open('maalinger_h.dat', 'r')
for line in file:
	cols = line.split()
	m.append( float(cols[0]) )
	h.append( float(cols[1]) )
file.close()

m_arr = np.array(m)
h_arr = np.array(h)

dA, dc, c, A = FYS2150lib.linfit(m_arr, h_arr)

print A, dA