# Trajectory from charged particules affected by Lorentz forces.
# From old Matlab code that had correct results (used as reference)

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# from field import field  # Use for debugging
from lorentz import lorentz
from euler_2Ddy import euler2d

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

# Box limits
x1 = -20
x2 = 20
y1 = -20
y2 = 20

# Calculate Fields and Forces for debugging
# E, B, theta = field(q, x0, y0, vx0, vy0, m, epsz, muz)
# F, Etot, Btot, Ey = lorentz(q, x0, y0, vx0, vy0, m, epsz, muz)
# print('Lorentz Forces')
# print('Fx, Fy, Fz')
# print(F)

# Define a vector to indicate if particule is still in the box
in_out = np.ones(len(q))

step = 0.01
x, y, vx, vy = x0, y0, vx0, vy0
xx, yy = [x0], [y0]


# for ii in range(100):  # Use this line for debugging
while sum(in_out) != 0:
    # Each time a particle is out of the box, we elimitate it's contribution
    # We use Lorentz forces to determine acceleration on particules
    F, Etot, Btot, Ey = lorentz(q, x, y, vx, vy, m, epsz, muz)
    ax = (in_out*F[0])/m
    ay = (in_out*F[1])/m
    # We use euler 2d dynamics to plot trajectory of particules
    x, y, vx, vy = euler2d(x, y, vx, vy, ax, ay, step)
    # We remove particles that get out of the box
    for p in range(len(q)):
        if x[p] <= x1 or x[p] >= x2 or y[p] <= y1 or y[p] >= y2:
            in_out[p] = 0
        else:
            xx.append(x)
            yy.append(y)
    print(in_out)


# Plot retults
fig, ax = plt.subplots(1)
box = patches.Rectangle((x1, y1), (x2-x1), (y2-y1),
                        linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(box)
plt.plot(xx, yy)
axes = plt.gca()
axes.set_xlim([x1-10, x2+10])
axes.set_ylim([y1-10, y2+10])
plt.show()
