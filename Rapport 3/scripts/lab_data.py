#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Contains all of the data collected in the
Elacticity lab, module 2 of FYS2150
author: Nicholas Karlsen
"""

from pylab import *
import scipy.constants as const
import FYS2150lib as fys


rcParams.update({'font.size': 13})  # Sets font size of plots

def weight_data(set=1):
    "set decides which data set the function returns."
    set = set.lower()   # Forces lowercase
    sets = ["masses", "rod"]
    # Mass of weights measured with balance
    m_a_balance = 500.1e-3
    m_b_balance = 1000.3e-3
    m_c_balance = 2000.5e-3

    # Mass of reference weights
    m_reference = array([0.5, 1.0, 2.0])
    m_reference_balance = array([500.0e-3, 999.9e-3, 2000.1e-3])  # Weighed

    # Using linear fit to correct for error in balance
    a, b, da, db = fys.linfit(m_reference, m_reference_balance)
    # Corrected masses
    m_a = (m_a_balance - b) / a     # approx 500g
    m_b = (m_b_balance - b) / a     # approx 1000g
    m_c = (m_c_balance - b) / a     # approx 2000g

    if set == sets[0]:  # Return corrected masses
        return m_a, m_b, m_c

    m_rod_ring = np.array([2482.7, 2482.5, 2482.1]) * 1e-3
    m_ring = 34.4 * 1e-3    #kg
    m_rod = (mean(m_rod_ring) - m_ring - b) / a  #kg


    if set == sets[1]:
        return m_rod

    if set not in sets:
        print "Invalid set"
        print "List of valid sets:", sets
        print "exiting..."
        exit()


def E_sound(f, L, d, M):
    '''
    Returns youngs modulus given
    f = root frequency
    L = lenght between knives
    d = diameter of rod
    M = mass of rod
    '''
    return (16.0 * M * L * f**2) / (np.pi * d**2)


def E_sound_error(E, sd, sf, sL, sM, d, f, L, M):
    return E * np.sqrt((2 * sd / d)**2 + (2 * sf / f)**2 +
                       (2 * sL / L)**2 + (2 * sM / M)**2)


d = np.array([15.98, 15.99, 15.99, 16.00,
              15.99, 15.99, 15.98, 15.99,
              15.99, 15.99]) * 1e-3
d_mean = np.mean(d)
d_err = np.sqrt(fys.stddev(d)[1]**2 + (0.01e-3)**2) # Std dev of mean + instrumentation error

f_root = 1213.72
f_err = 0.04  # resolution of FFT
L_err = 1e-3
M_err = 1e-3

l_BC_outer = 133.9 * 1e-2
l_knife_diameter = 4.09 * 1e-3
l_BC = l_BC_outer - l_knife_diameter

E_sound = E_sound(f=f_root,
                  L=l_BC,
                  d=d_mean,
                  M=weight_data("rod"))

print "E from root f = %e" % E_sound

print "E_err root = %e" % E_sound_error(E=E_sound,
                                        sd=d_err,
                                        sf=f_err,
                                        sL=L_err,
                                        sM=M_err,
                                        d=d_mean,
                                        f=f_root,
                                        L=l_BC,
                                        M=weight_data("rod"))


def experiment1_data():
    m_a, m_b, m_c = weight_data("masses")
    mass_dat = array(
        [0, m_a, m_b, m_a + m_b, m_c, m_a + m_c,
         m_b + m_c, m_a + m_b + m_c])              # [Kg]

    # Round 1: (in order)
    h_1 = array([9.44, 8.72, 8.00, 7.28, 6.58, 5.84, 5.15, 4.43]) * 1e-3  # [m]
    # Round 2: (in order)
    h_2 = array([9.42, 8.70, 7.98, 7.26, 6.53, 5.80, 5.09, 4.39]) * 1e-3  # [m]
    # Round 3: (in order)
    h_3 = array([9.42, 8.71, 7.98, 7.26, 6.53, 5.80, 5.09, 4.37]) * 1e-3  # [m]
    # Round 4: (in order)
    h_4 = array([9.41, 8.69, 7.97, 7.25, 6.52, 5.79, 5.08, 4.36]) * 1e-3  # [m]
    # Round 5: (in order)
    h_5 = array([9.42, 8.70, 7.98, 7.26, 6.70, 5.87, 5.19, 4.51]) * 1e-3  # [m]

    h_mean = (h_1 + h_2 + h_3 + h_4 + h_5) / 5.0

    A, B, dA, dB = fys.linfit(mass_dat, h_mean)

    mass = linspace(0, 3.5, 8)
    h_mass = A * mass + B  # h(m)


    def plotdata():
        h_sets = [h_1, h_2, h_3, h_4, h_5]
        plot(mass, h_mass, label="Linear fit")
        # errorbar(mass, m * mass + c, yerr=dm, color='blue', fmt='o', label='Error Range')

        for dat in h_sets:
            plot(mass_dat, dat, "x", color="r")
        plot(NaN, NaN, "xr", label="Data points")
        xlabel("mass [kg]")
        ylabel("h(m) [m]")
        ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        legend()
        title("Linear fit of mean deflection data; h(m) = Am + B\n$\delta A =$ %.2e" % dA)
        savefig("figs/h_m_fig.png")
        close()
    plotdata()

    def plot_stddev():
        """Plots the standard deviation of h(m)
        as m is increased"""
        deviation = np.zeros(len(h_1))
        for i in xrange(len(h_1)):
            deviation[i] = fys.stddev(array([h_1[i],
                                             h_2[i],
                                             h_3[i],
                                             h_4[i],
                                             h_5[i]]))[0]
        plot(mass_dat, deviation, linestyle="--")
        plot(mass_dat, deviation, "o")
        ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        title("Standard deviation of deflection for each m\n")
        xlabel("Load [kg]")
        ylabel("$\sigma$ (Std. dev.)")
        savefig("figs/h_m_deviation.png")
        close()
    plot_stddev()

    # lengde mellom yttersidene til festepunktene til knivene
    # PEE WEE 2m Y612CM LUFKIN +- 0.01cm
    l_AB = 133.9 * 1e-2  # [m]
    # diameter til festepunkter
    # Moore & Wright 1965 MI +- 0.01mm
    l_AB_diameter = 4.09 * 1e-3  # [mm]
    # anta festepunktet er paa midtden saa trekk fra diameter totalt sett
    l = l_AB - l_AB_diameter
    
    #Maalinger av stangens diameter d paa forskjellige punkter
    # Moore & Wright 1965 MI +- 0.01mm
    d = array([15.98, 15.99, 15.99, 16.00, 15.99, 15.99, 15.98, 15.99, 15.99, 15.99]) * 1e-3  # [m]
    d_mean = mean(d) #m

    E = (4.0 * l**3 * const.g / (3 * pi * abs(A) * d_mean**4))
    print "E from deflection = %e"%E

def experiment_2():
    ''' Data pertaining to the audio exp.'''


experiment1_data()
