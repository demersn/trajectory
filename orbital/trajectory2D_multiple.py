# We will use [euler 2D dynamics] to simulate mouvement with multiple planets
# Cartesian coordinates will be used
import numpy as np
import matplotlib.pyplot as plt
from euler_2Ddy import euler2d

# Parameters
# [1, 2, 3, etc] for planet, s for ship
# First planet
m_1 = 5.972e24  # kg
r_1 = 6371e3  # m
x1, y1 = 0, 0  # planet position
# Second planet
m_2 = m_1/1.2  # kg
r_2 = r_1/2  # m
x2, y2 = 10*r_1, 10*r_2  # planet position
# Add more planets here
# Ship
m_s = 1000  # kg

# Initial condition INPUT
v0 = 11000  # m/s
theta_p = 180  # position angle, degrees, [+] counter-clockwise, 0 on 'the left'
theta_l = theta_p+65  # launch angle, degrees,  [+] counter-clockwise
r0 = r_1  # initial position of the ship
step = 1  # seconds (your milage may vary)
n_max = 100000  # to limit the max calculation

# Initial conditions FROM input
x0, y0 = r0*np.cos(np.deg2rad(theta_p)), r0*np.sin(np.deg2rad(theta_p))
vx0, vy0 = v0*np.cos(np.deg2rad(theta_l)), v0*np.sin(np.deg2rad(theta_l))
x, y, vx, vy = x0, y0, vx0, vy0
xx = np.array([x1, x2])  # Add all planets here
yy = np.array([y1, y2])  # and here
mm = np.array([m_1, m_2])  # and here
xplot = [x0]
yplot = [y0]

# Iterate up to n_max
for ii in range(0, n_max):
    # Gravitationnal force
    G = 6.67408e-11  # m**3 kg**-1 s**-2
    r = np.sqrt((xx-x)**2+(yy-y)**2)
    F = (G*mm*m_s)/(r**2)
    Fx = F*np.cos(np.arctan2(yy-y, xx-x))
    Fx = sum(Fx)
    Fy = F*np.sin(np.arctan2(yy-y, xx-x))
    Fy = sum(Fy)

    # Acceleration from F=ma
    ax = Fx/m_s
    ay = Fy/m_s

    # Next position and speed from Euler
    x, y, vx, vy = euler2d(x, y, vx, vy, ax, ay, step)
    xplot.append(x)
    yplot.append(y)

    # Stop if we meet planet surface
    if r[0] < r_1 or r[1] < r_2 and ii > 1:
        print('Landed on (%d, %d)' % (x, y))
        break

# Plot
fig, axes = plt.subplots(1)  # Initiate plot
planet_1 = plt.Circle((x1, y1), r_1, color='k')  # Draw planet_1
axes.add_artist(planet_1)  # Show planet_1
planet_2 = plt.Circle((x2, y2), r_2, color='k')  # Draw planet_2
axes.add_artist(planet_2)  # Show planet_2
# Add more planets here
plt.plot(xplot, yplot)  # Plot spaceship trajectory
plt.gca().set_aspect('equal', adjustable='box')  # Same scale on axis so circles are round
max_xy = max(max(np.absolute(xplot)), max(np.absolute(yplot)))
plot_lim = 1.25*((x1+x2)+max_xy)
axes.set_xlim([-plot_lim, plot_lim])
axes.set_ylim([-plot_lim, plot_lim])
plt.show()  # Show plot
