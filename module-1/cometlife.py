# cometlife.py -- how many orbits does a sublimating comet have left?
# Reference version of the Pod 0 program. Everything in SI units.
from math import sqrt, pi

R = float(input("Enter comet radius in meters: "))  # comet radius, m

L = 3.8e26          # solar luminosity, J/s
GM = 1.3271e20      # G times the Sun's mass, m^3/s^2
h_ice = 2.5e6       # energy to sublimate 1 kg of ice, J/kg
AU = 1.49e11        # meters per AU

rho = 500.0         # comet density, kg/m^3
A = 0.0             # albedo
a = 3.12 * AU       # semi-major axis, m
e = 0.5             # eccentricity

H_sol = (pi / 2) * (1 - A) * R**2 * L / sqrt(GM) / sqrt(a * (1 - e**2))   # J absorbed per orbit
dM = H_sol / h_ice                                                       # kg lost per orbit
dr = dM / (4 * pi * rho * R**2)                                          # m of radius lost per orbit

print(f"Comet radius: {R:.1f} m")
print(f"Radius lost per orbit: {dr:.10f} m")
print(f"Orbits left: {R / dr:.0f}")
