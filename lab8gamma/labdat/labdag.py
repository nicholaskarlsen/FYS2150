import numpy as np
import matplotlib.pyplot as plt
import FYS2150lib

tellinger = np.array([
    6, 2, 3, 2, 2, 2, 5, 5, 3, 4, 3, 5, 4, 7, 4, 2, 3, 2, 2, 4, 6, 2, 3, 2, 6, 3, 7, 10, 6, 4, 
    2, 4, 6, 3, 5, 3, 1, 5, 4, 9, 5, 7, 1, 5, 1, 6, 4, 4, 3, 4, 4, 2, 5, 3, 2, 4, 2, 3, 1, 6, 
    3, 4, 3, 2, 2, 7, 2, 2, 2, 2, 5, 2, 3, 1, 0, 6, 3, 6, 1, 2, 2, 6, 1, 2, 3, 6, 4, 4, 4, 3,
    5, 0, 2, 2, 3, 3, 7, 3, 8, 3
    ])

plt.hist(tellinger)
plt.show()
print "mean:", np.mean(tellinger)
print "\nstd dev.:", FYS2150lib.stddev(tellinger)
print "\nsqrt mean:", np.sqrt(np.mean(tellinger))
