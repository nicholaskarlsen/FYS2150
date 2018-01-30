# coding=UTF-8
# by nicholas karlsen
import numpy as np
import matplotlib.pyplot as plt

end_time = 25            # number of seconds of data
n = int(1e3 * end_time)  # number required for 1khz data
A = 10                   # amplitude
x = np.linspace(0, end_time, int(n))

mu = 0              # Mean used for noise, set to 0 so it varies between +/-
sigma = 0.2 * A     # Standard deviation used for noise
drift = 0.05 * A * x
noise = np.random.normal(mu, sigma, n)

data = A * np.sin(x) + noise + drift

def signal_plot():  # Question 2
    plt.plot(x, data)
    plt.ylabel("Volt [V]")
    plt.xlabel("Time [s]")
    plt.title("Signal with noise and drift")
    plt.show()
signal_plot()

def histogram1():   # Question 3
    """
    The arc is a bit wider than i expect, the dimple in the middle is
    presumably due to the drift.
    """
    plt.hist(data, bins=30, rwidth=0.75)
    plt.title("Distribution of measured voltages")
    plt.xlabel("Volt [V]")
    plt.show()
histogram1()

def histogram2():  #  Question 4
    plt.hist(noise, bins=30, rwidth=0.75)
    plt.title("Distribution of Noise")
    plt.xlabel("Noise")
    plt.show()
histogram2()

def histogram3():   # Question 5
    """
    This is clearly wrong, and i am not sure if it is due to a programming
    error, or a lack of understanding. Would apreciate some direction on this
    part. Tested for different values of n, if too large it resulted in a 
    "box distribution" and smaller ones all sufferes from the same issue as 
    the one with my provided values.
    """
    y = np.linspace(-20, 40, 1e4)
    norm_line = np.exp(-(y - np.mean(data))**2/(2 * sigma**2)) / np.sqrt(2 * np.pi * sigma**2)
    plt.plot(y, norm_line)
    plt.hist(data, bins=30, rwidth=0.75, normed=1)
    plt.title("Normalised distribution of measured voltages")
    plt.xlabel("Volt [V]")
    plt.show()
histogram3()