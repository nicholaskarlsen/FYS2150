import numpy as np
import matplotlib.pyplot as plt

periods = np.array([
    14.14, 14.39, 14.39, 14.40, 14.29, 14.39, 14.29, 14.34, 14.20, 14.52
    ])

print "Mean period", np.mean(periods)
print "standard dev", np.std(periods)

#plt.plot(periods, "x")
#plt.show()