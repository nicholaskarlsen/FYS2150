#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generates the same figures as FFTlyd.m
author: Nicholas Karlsen
"""
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np


# Sets font size of matplot
plt.rcParams.update({'font.size': 12})


def import_matlab(filename):
    # Opens .mat file
    mfile = sio.loadmat(filename)
    # Fetches data
    data = mfile.get("data")
    energi = mfile.get("energi")
    fut = mfile.get("fut")
    L = mfile.get("L")
    t = mfile.get("t")

    return data, energi, fut, L, t


rel_path = "data/"
n = 1
mat_file = "forsok%i.mat" % n


def raw_fig(filename):
    data, energi, fut, L, t = import_matlab(filename)
    plt.plot(t, data)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.title("Recorded audio of attempt no. 1")
    plt.savefig("raw_exp2_1.png")
    plt.close()


raw_fig(rel_path + "forsok1.mat")


def figure1(filename):
    data, energi, fut, L, t = import_matlab(filename)
    fut = np.transpose(fut)
    fh = int(len(energi) / 2.0)   # half lenght of data
    # Only plot first half of data, as FF mirrors in half-way point.
    plt.plot(fut[:fh], energi[:fh])
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.title("FFT of attempt no. 1 data")
    plt.savefig("energy_exp2_1.png")
    plt.close()


figure1(rel_path + "forsok1.mat")


eigenfreqs = []


def figure2(filename):
    data, energi, fut, L, t = import_matlab(filename)
    fut = np.transpose(fut)

    fh = int(len(energi) / 2.0)   # half lenght of data
    ipeak = np.argmax(energi[:fh])

    eigenfreqs.append(fut[ipeak])

    i = ipeak
    while energi[i] > np.amax(energi[:fh]) * 0.01:
        i -= 1

    j = ipeak
    while energi[j] > np.amax(energi[:fh]) * 0.01:
        j += 1

    plt.plot(fut[i:j], energi[i:j])
    plt.plot(fut[ipeak], energi[ipeak], "o", label="%.2fHz" % fut[ipeak])

figure2(rel_path + "forsok1.mat")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xticks(rotation=10)
plt.title("FFT of all attempts")
plt.savefig("freq_exp2_1.png")
plt.close()


for i in range(1, 8):
    figure2(rel_path + "forsok%i.mat" % i)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.legend()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xticks(rotation=10)
plt.savefig("freq_exp2_all.png")
plt.close()