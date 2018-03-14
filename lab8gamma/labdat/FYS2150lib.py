# By Nicholas Karlsen
import numpy as np

def stddev(x):
    "Eqn D. Page 24 squires"
    n = len(x)
    sigma = np.sqrt(float(np.sum(x**2) - 1.0/n * np.sum(x)**2)/(n - 1))
    sigma_m = np.sqrt(float(np.sum(x**2) - 1.0/n * np.sum(x)**2)/(n*(n - 1)))
    return sigma, sigma_m

def vel(fm, f):
    """
    Returns the velocity of a moving body given a measured freq
    emitted from it.
    f = frequency of object while at rest
    fw = measured frequency of object
    """
    T = 21.1            # Temperature in lab
    c = 331.1+(0.606 * T)  # Speed of sound in air
    return c - float(c*f) / fm

def linfit(x, y):
    n = np.size(y)
    D = np.sum(x**2) - (1.0 / n) * np.sum(x)**2
    E = np.sum(x*y) - (1.0 / n) * np.sum(x) * np.sum(y)
    F = np.sum(y**2) - (1.0 / n) * np.sum(y)**2

    dm = np.sqrt(1.0 / (n - 2) * (D * F - E**2) / D**2)
    dc = np.sqrt(1.0 / (n - 2) * (float(D) / n + np.mean(x)) * ( (D*F - E**2) / (D**2) ))
    m = float(E) / D
    c = np.mean(y) - m*np.mean(x)

    return dm, dc, c, m