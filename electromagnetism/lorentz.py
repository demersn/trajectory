# Calculation of Lorentz forces between particles.
# This fuction requires the use of the [field] function

import numpy as np
from field import field


# Call with F = lorentz(q, x0, y0, vx0, vy0, m, epsz, muz)
def lorentz(q, x0, y0, vx0, vy0, m, epsz, muz):
    # We use the [field] function
    E, B, theta = field(q, x0, y0, vx0, vy0, m, epsz, muz)
    v = np.array([vx0, vy0, np.zeros(len(vx0))])
    Ex = E.dot(np.array(np.cos(theta)))
    Ey = E.dot(np.array(np.sin(theta)))
    Etot = [np.sum(Ex, axis=1), np.sum(Ey, axis=1), np.zeros(len(vx0))]
    Btot = [np.zeros(len(vx0)), np.zeros(len(vx0)), np.sum(B, axis=1)]
    # Cross products
    Fcross = np.cross(np.swapaxes(v, 0, 1), np.swapaxes(Btot, 0, 1))
    Fcross = np.swapaxes(Fcross, 0, 1)
    # Lorentz = E * Fcross
    F = q*[Etot[0]+Fcross[0], Etot[1]+Fcross[1], Etot[2]+Fcross[2]]

    return F, Etot, Btot, Ey
