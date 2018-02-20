# By Nicholas Karlsen
import scipy.io as sio
import numpy as np


def importdata(filename):
    "Used to import data from .m file"
    data = sio.loadmat(filename)
    R = data.get("R")  # Change R to variable name in .m file
    return R


def Temp(R):
    a = 8.420e-004
    b = 2.068e-004
    c = 8.591e-008
    return (1.0 / (a + b * np.log(R) + c * (np.log(R))**3)) - 273.16


if __name__ == '__main__':
    print Temp([1e6, 20e3])
