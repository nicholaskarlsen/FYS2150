from pylab import *

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
    y = array(y)
    z = array(z)

    return y, z

y1, z1 = readfile("polarisering1.dat")

print "plotting y1"
plot(y1)
print "plotting z1"
plot(z1)
savefig("temp.png")
close()
print "Done"