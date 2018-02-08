import numpy as np
import matplotlib.pyplot as plt

periods = np.array([
    14.14, 14.39, 14.39, 14.40, 14.29, 14.39, 14.29, 14.34, 14.20, 14.52
    ])
print "Stopwatch:"
print "Mean period", np.mean(periods)
print "standard dev", np.std(periods)

periods2 = np.array([
    116, 121, 128])

print "\nHourglass:"
print "Mean period", np.mean(periods2)
print "standard dev", np.std(periods2)