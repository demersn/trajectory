# Trajectory from charged particules affected by Lorentz forces

import numpy as np
import math
from field import field
from lorentz import lorentz

# Lorentz Forces Test

# Constants
m = 9.109e-31  # [kg]
epsz = 1e-9/36*math.pi  # epsilon zero [F/m]
muz = (4e-7)*math.pi  # mu zero [H/m]

# Initial conditions
q = 1.602e-19*np.array([1, 1, 1, 1, -1, -1, -1, -1])
x0 = np.array([10,  10, -10, -10,  0,   10, -10,  0])  # m
y0 = np.array([10, -10,  10, -10, -10,  0,   0,  10])  # m
vx0 = np.array([-5,  0,  0,  5,  5,  0,  0, -5])  # ms^-1
vy0 = np.array([0,  5, -5,  0,  0,  5, -5,  0])  # ms^-1


E, B, theta = field(q, x0, y0, vx0, vy0, m, epsz, muz)
F, Etot, Btot, Ey = lorentz(q, x0, y0, vx0, vy0, m, epsz, muz)

print('Lorentz Forces')
print('Fx')
print(F[0])
print('Fy')
print(F[1])
print('Fz')
print(F[2])
