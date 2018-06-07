import numpy as np
import matplotlib.pyplot as plt
import FYS2150lib

# LAB A
# Tellinger fra Cs-137 fra GM-ror.
# d = 22mm
# r = (11.1 + ) / 2
tellinger1 = np.array([
    6, 2, 3, 2, 2, 2, 5, 5, 3, 4, 3, 5, 4, 7, 4, 2, 3, 2, 2, 4, 6, 2, 3, 2, 6, 3, 7, 10, 6, 4, 
    2, 4, 6, 0, 3, 5, 3, 1, 5, 4, 9, 5, 7, 1, 5, 1, 6, 4, 4, 3, 4, 4, 2, 5, 3, 2, 4, 2, 3, 1, 6, 
    3, 4, 3, 2, 2, 7, 2, 2, 2, 2, 5, 2, 3, 1, 0, 6, 3, 6, 1, 2, 2, 6, 1, 2, 3, 6, 4, 4, 4, 3,
    5, 0, 2, 2, 3, 3, 7, 3, 8, 3
    ])

tellinger = np.array([
    6, 2, 3, 2, 2, 2, 5, 5, 3, 4, 3, 5, 4, 7, 4, 2, 
    3, 2, 2, 4, 6, 2, 3, 2, 6, 3, 7, 10, 6, 4, 2, 4,
    6, 0, 3, 5, 3, 1, 5, 4, 9, 5, 7, 1, 5, 1, 6, 4, 4,
    0, 3, 4, 4, 2, 5, 3, 2, 4, 2, 3, 1, 6, 3, 4, 3, 2, 
    2, 7, 2, 2, 2, 2, 5, 2, 3, 1, 0, 6, 3, 6, 1, 2, 3, 
    6, 1, 2, 3, 6, 4, 4, 4, 3, 5, 0, 2, 2, 3, 3, 7, 3, 8,
    3
    ])

# MERK Tellinger 1 var notert ned feil. Tellinger er basert paa daniels journal.
# Dobbelt sjekk at verdiene stemmer.

print len(tellinger)

mean = np.mean(tellinger)
print "mean:", mean
print "\nstd dev.:", FYS2150lib.stddev(tellinger)
print "\nsqrt mean:", np.sqrt(mean)


def theoretical_poisson(N, m, k):
    y = np.zeros(k)
    y[0] = N*np.exp(-m)
    for i in range(1, k):
        y[i] = (m / (i)) * y[i-1]
    return y

print theoretical_poisson(100, mean, 11)

plt.hist(tellinger, label="Measured", bins=10)
plt.plot(theoretical_poisson(101, mean, 10), label="Predicted")
plt.title("Number of gamma particles emmitted by Cs-137 in 1 second")
plt.legend()
plt.close()

# LAB B
t = np.array([
    7*60 + 50.15, 4*60 + 44.16, 2*60 + 43.45,
    1*60 + 38.48, 1*60 + 0.04, 0*60 + 45.41
    ])

#Plater
A = np.array([0.5, 0.52, 0.53, 0.51]) * 10**(-2)
B = np.array([0.5, 0.51, 0.505, 0.51]) * 10**(-2)
C = np.array([0.510, 0.510, 0.505, 0.500]) * 10**(-2)
D = np.array([0.490, 0.490, 0.490, 0.490]) * 10**(-2)
E = np.array([0.505, 0.505, 0.505, 0.510]) * 10**(-2)

thickness = []
for plate in [A, B, C, D, E]:
    thickness.append(np.mean(plate))
thickness = np.array(thickness)
skjerming = np.array([
    sum(thickness),
    sum(thickness[1:-1]),
    sum(thickness[2:-1]),
    sum(thickness[3:-1]),
    sum(thickness[4:-1]),
    0
    ])
print "\nlab B"
print skjerming



