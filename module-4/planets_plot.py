# planets_plot_starter.py -- the ten planets as arrays, ready to plot (Pod 6). Copy this file to planets_plot.py and work on the copy.
# Run from the repository folder:  python module-4/planets_plot.py
import numpy as np
import matplotlib.pyplot as plt

SIGMA = 5.67e-8          # Stefan-Boltzmann constant, W m^-2 K^-4
L_SUN = 3.8e26           # solar luminosity, W
AU = 1.496e11            # meters per AU

name = np.array(["Earth", "Mars", "HD 209458 b", "51 Peg b", "TRAPPIST-1 e",
                 "Kepler-22 b", "55 Cnc e", "HD 189733 b", "Kepler-452 b", "Proxima b"])
lum = np.array([1.0, 1.0, 1.6, 1.3, 0.00055, 0.79, 0.58, 0.34, 1.2, 0.0016])        # star luminosity, solar units
dist = np.array([1.000, 1.524, 0.047, 0.052, 0.029, 0.85, 0.0154, 0.031, 1.046, 0.0485])   # distance, AU


def t_eq(L, d):
    """Equilibrium temperature (K) at distance d (m) from a star of luminosity L (W)."""
    return (L / (16 * np.pi * SIGMA * d**2)) ** 0.25
d = np.linspace(0.01, 2.0, 200)


if __name__ == "__main__":
    T = t_eq(lum * L_SUN, dist * AU)
    T_curve = t_eq(L_SUN, d * AU)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(16, 8))
    a1.scatter(dist, T)
    a1.plot(d, T_curve, color='red', label='Sun')
    a1.legend()
    a1.set_xlabel("Distance (AU)")
    a1.set_ylabel("Equilibrium Temperature (K)")
    a1.set_title("Linear Scale")
    a2.scatter(dist, T)
    a2.plot(d, T_curve, color='red', label='Sun')
    a2.legend()
    a2.set_xlabel("Distance (AU)")
    a2.set_ylabel("Equilibrium Temperature (K)")
    a2.set_title("Log Scale")
    a2.set_xscale("log")
    a2.set_yscale("log")
    for n, x, y in zip(name, dist, T): a2.annotate(n, (x, y), fontsize=7)
    for n, x, y in zip(name, dist, T): a1.annotate(n, (x, y), fontsize=7)
    fig.savefig("module-4/planets.png", dpi=150)
    print("wrote module-4/planets.png")
