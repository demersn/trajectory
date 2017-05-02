# Calculation of E and B field from the position of the particles

import numpy as np


# Call with E, B, theta = field(q, x0, y0, vx0, vy0, m, epsz, muz)
def field(q, x0, y0, vx0, vy0, m, epsz, muz):
    E = np.zeros((len(q), len(q)))
    B = np.zeros((len(q), len(q)))
    theta = np.zeros((len(q), len(q)))
    # store = []
    for ii in range(len(q)):
        for jj in range(len(q)):
            # Remove cases where i == j
            if ii == jj:
                E[ii][jj] = 0
                B[ii][jj] = 0
                theta[ii][jj] = 0
            else:
                # Vector between particles
                vect_i2j = np.array([x0[jj]-x0[ii], y0[jj]-y0[ii], 0])
                # store.append(vect_i2j)
                # q*v
                qv = q[jj]*np.array([vx0[jj], vy0[jj], 0])
                # r_hat, unit vector from part. i to j
                rhat = vect_i2j / np.linalg.norm(vect_i2j)
                # Forces arrays
                E[ii][jj] = q[jj] / (4*np.pi*epsz*(vect_i2j[0]**2+vect_i2j[1]**2))
                # np.arctan2 is used to get the direction as well as the angle
                theta[ii][jj] = np.arctan2(vect_i2j[1], vect_i2j[0])
                # theta = np.swapaxes(theta, 0, 1)
                # numpy.cross is used to get the correct sign for B
                B[ii][jj] = (muz*sum(np.cross(qv, rhat))) / (
                    4*np.pi*(vect_i2j[0]**2+vect_i2j[1]**2))
                # As the charge is included in the q vector, direction of B is
                # not subject to change
    return E, B, theta
