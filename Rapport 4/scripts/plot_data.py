import numpy as np
import matplotlib.pyplot as plt

#pltrcParams.update({'font.size': 13})  # Sets font size of plots

def nuOlje(T):
    # Beregne kinematisk (nu) og dynamisk (mu) vikositet for Shell-oljen nr. 68
    # som en funksjon av temperatur i grader C.
    #
    # nu er oppgitt i centistokes (cSt): 1 cSt = 10^-6 m^2/s.
    a = np.array([1033.05, - 90.7992, 4.08103, - 0.104967,
                  0.00143595, - 8.02259 * 10**-6])
    rho = 886    # kg/m^3 ved 15 C

    Tpoly = np.array([1, T, T**2, T**3, T**4, T**5])

    nu = sum(a * Tpoly)
    mu = rho * nu

    return mu


def readlabdat(filename):
    """
    Used to read the file which stores the parameters of the
    sphere
    """
    vids = []; mass = []; radius = []; temp = []
    v = []

    file = open(filename, "r")
    for line in file:
        cols = line.split("&")
        mass.append(cols[1])
        radius.append(cols[2])
        v.append(cols[3])
        temp.append(cols[-2])
        vids.append(cols[-1])
    file.close()

    return mass, radius, temp, vids, v
mass, radius, temp, vids, v = readlabdat("data/labdata.dat")

for listname in [mass, radius, temp, vids, v]:
    listname.pop(6)
    listname.pop(0)
    listname.pop(0)
    listname.pop(-1)

mass = np.array(mass, dtype=float)
radius = np.array(radius, dtype=float)
temp = np.array(temp, dtype=float)
v = np.array(v, dtype=float)

mu_oil = []
for val in temp:
    mu_oil.append(val)
mu_oil = np.array(mu_oil, dtype=float)

g = 9.80665     # Standard Gravity
rho_oil = 886   # Density of Hydraulic oil at 15C
Fg = g * mass
Fd = Fg - (g * rho_oil * np.pi * radius**3 * (4.0 / 3.0))

CR = Fd / (rho_oil * v**2 * radius**2)
CS = Fd / (mu_oil * v * radius)
Re = rho_oil * v * radius / mu_oil

plt.plot(Fg / radius, v, "x")
plt.ylabel("$v_c \enspace  [ms^{-1}]$")
plt.xlabel("$F_g / r \enspace [Nm^{-1}]$")
plt.grid("on")
plt.savefig("figs/v_fgr.png")
plt.show()

plt.plot(Fg / radius**2, v**2, "x")
plt.ylabel("$v_c^2 \enspace  [m^2s^{-2}]$")
plt.xlabel("$F_g / r^2 \enspace [Nm^{-2}]$")
plt.grid("on")
plt.savefig("figs/v2_fgr2.png")
plt.show()

plt.plot(Re, CS, "x")
plt.ylabel("$C_S$")
plt.xlabel("$R_e$")
plt.grid("on")
plt.savefig("figs/CS_RE.png")
plt.show()

plt.plot(Re, CR, "x")
plt.ylabel("$C_R$")
plt.xlabel("$R_e$")
plt.grid("on")
plt.savefig("figs/CR_RE.png")
plt.show()