import scipy.io as sio
import numpy as np

def uncertainties(x, y):
    n = len(y)
    D = sum(x**2) - (1.0 / n) * sum(x)**2
    E = sum(x*y) - (1.0 / n) * sum(x) * sum(y)
    F = sum(y**2) - (1.0 / n) * sum(y)**2
    
    dm = np.sqrt(1.0 / (n - 2) * (D * F - E**2) / D**2)
    dc = np.sqrt(1.0 / (n - 2) * (float(D) / n + np.mean(x))\
            * ( (D*F - E**2) / (D**2) ))
    m = float(E) / D
    c = np.mean(y) - m*np.mean(x)

    return dm, dc, m, c