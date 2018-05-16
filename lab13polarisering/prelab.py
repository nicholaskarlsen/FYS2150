import numpy as np
import matplotlib.pyplot as plt

def readfile(filename):
    print "Opening file"
    file = open(filename, "r")
    y = []
    z = []
    for line in file:
        col = line.split()
        y.append(col[0])
        z.append(col[1])
    file.close()
    print "Closing file"
    yz = np.array([y, z])
    np.save(filename.split(".")[0], yz)
    return 

#readfile("polarisering1.dat")
#readfile("polarisering2.dat")
#readfile("polarisering3.dat")

yz1 = np.load("polarisering1.npy")
plt.plot(yz1[0])
plt.show()
#yz2 = np.load("polarisering2.npy")
#yz3 = np.load("polarisering3.npy")
