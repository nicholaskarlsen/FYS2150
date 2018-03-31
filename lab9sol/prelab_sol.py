# By Nicholas Karlsen
# Prelab for Lab no. 10; The solar panel
from pylab import *
import FYS2150lib as fys

V = linspace(0, 0.6, 7)
I = array([0.200, 0.195, 0.190, 0.180, 0.150, 0.080, 0.005])
P = V * I
print I[0] * V[-1] * 100 / 60.0