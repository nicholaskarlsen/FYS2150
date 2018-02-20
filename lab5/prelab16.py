import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

data = sio.loadmat("maalesett.mat")    
X = data.get("datasett")


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

dm, dc, c, m = prelab_func(X[:, 0], X[:, 1])

plt.plot(X[:, 0], X[:, 1])
plt.xlabel("n")
plt.ylabel("$f^{-1}(...)$")
plt.close()

print m
D =  1.0 / (m**2)
print D

dD = D*(2*(dm / m))

print dD