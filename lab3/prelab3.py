import scipy.io as sio
import numpy as np

data = sio.loadmat("linjedata.mat")

x = data.get("x")
y = data.get("y")
a = data.get("a")
b = data.get("b")

def prelab_func(x, y):
    n = np.size(y)
    D = np.sum(x**2) - (1.0 / n) * np.sum(x)**2
    E = np.sum(x*y) - (1.0 / n) * np.sum(x) * np.sum(y)
    F = np.sum(y**2) - (1.0 / n) * np.sum(y)**2
    
    dm = np.sqrt(1.0 / (n - 2) * (D * F - E**2) / D**2)
    dc = np.sqrt(1.0 / (n - 2) * (float(D) / n + np.mean(x)) * ( (D*F - E**2) / (D**2) ))
    m = float(E) / D
    c = np.mean(y) - m*np.mean(x)

    return dm, dc, c, m

print "Calculated values from function:\ndm = %f \ndc = %f \nm = %f \nc = %f" % prelab_func(x, y)

print "Imported values from linjedata.mat:\na = %f\nb = %f" % (a, b)

# Output in terminal
"""
nick@thinkpad:~/Documents/uio/FYS2150/lab3$ python prelab3.py 
Calculated values from function:
dm = 0.329644 
dc = 0.385369 
m = 3.687948 
c = 4.970661
Imported values from linjedata.mat:
a = 3.500000
b = 5.000000
"""
