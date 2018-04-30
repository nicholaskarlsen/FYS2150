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
    vids = []; mass = []; diameter = []; temp = []
    v = []; ty=[]

    file = open(filename, "r")
    for line in file:
        cols = line.split("&")
        ty.append(cols[0])
        mass.append(cols[1])
        diameter.append(cols[2])
        v.append(cols[3])
        temp.append(cols[-2])
        vids.append(cols[-1])
    file.close()

    return mass, diameter, temp, vids, v, ty

mass, diameter, temp, vids, v, ty = readlabdat("data/labdata.dat")

for listname in [mass, diameter, temp, vids, v, ty]:
    listname.pop(6)
    listname.pop(0)
    listname.pop(0)
    listname.pop(-1)

mass = np.array(mass, dtype=float) * 1E-3
radius = (np.array(diameter, dtype=float) / 2.0) * 1E-3
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

plt.figure(figsize=(8, 4), dpi=100)
plt.plot(Fd / radius, v, "ro")
plt.ylabel("$v_c \enspace  [ms^{-1}]$")
plt.xlabel("$F_d / r \enspace [Nm^{-1}]$")
for i in range(len(v)):
    plt.annotate(vids[i].strip()[:2], (Fd[i] / radius[i], v[i]))
plt.grid("on")
plt.tight_layout()
plt.savefig("figs/v_fgr.png", dpi=200)
plt.close()

plt.figure(figsize=(8, 4), dpi=100)
plt.plot(Fd / radius**2, v**2, "ro")
plt.ylabel("$v_c^2 \enspace  [m^2s^{-2}]$")
plt.xlabel("$F_d / r^2 \enspace [Nm^{-2}]$")
for i in range(len(v)):
    plt.annotate(vids[i].strip()[:2], (Fd[i] / radius[i]**2, v[i]**2))
plt.grid("on")
plt.tight_layout()
plt.savefig("figs/v2_fgr2.png")
plt.close()

plt.figure(figsize=(8, 4), dpi=100)
plt.plot(Re, CS, "ro", label="Data points")
plt.ylabel("$C_S$")
plt.xlabel("$R_e$")
for i in range(len(v)):
    plt.annotate(vids[i].strip()[:2], (Re[i], CS[i]))
plt.grid("on")
plt.tight_layout()
plt.legend()
plt.savefig("figs/CS_RE.png")
plt.close()

plt.figure(figsize=(8, 4), dpi=100)
plt.plot(Re[:-1], CR[:-1], "ro")
plt.ylabel("$C_R$")
plt.xlabel("$R_e$")
for i in range(len(v)-1):
    plt.annotate(vids[i].strip()[:2], (Re[i], CR[i]))
plt.grid("on")
plt.tight_layout()
plt.savefig("figs/CR_RE.png")
plt.close()

for i in range(len(Re)):
    print "r = %5.2em | m = %5.2e | Re = %4.2f | CR = %4.2f | CS = %4.2f | %s" %(radius[i],mass[i], Re[i], CR[i], CS[i], vids[i].strip()[:2])


outfile = open("data/FINAL_table2.dat", "w")
outfile.write("Type &  Mass [g] &  Radius [mm] & $v_c$ [ms$^{-1}$] & $R_e$ & $C_S$ & $ C_R$ & FPS  &  T [$^\circ$C]  &  Label \\\ \hline \n")
for row in range(len(mass)):
    outfile.write("%s"%ty[row].strip() + " & " + "%.2f"%(mass[row] * 1E3) + " & " + "%.2f"%(radius[row]*1E3) + " & " + "%.3f"%v[row] + " & " + "%.3f"%Re[row] + " & " + "%.3f"%CS[row] + "&" + "%.3f"%CR[row] + " & " + "100" + " & " + "%.1f"%temp[row] + "&"+ "%s"%(vids[row].strip()[:2]) +"\\\ \n")


for i in range(len(mass)):
    print vids[i].strip()[:2], "%.2e"%(mass[i] / (np.pi * radius[i]**3 * (4.0 / 3.0)))