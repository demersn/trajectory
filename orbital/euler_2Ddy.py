# Euler free body dynamics equations in 2 dimensions


# Input position, speed, accelleration and step
def euler2d(x, y, vx, vy, ax, ay, step):
    x_next = x+step*vx
    y_next = y+step*vy
    vx_next = vx+step*ax
    vy_next = vy+step*ay
    return x_next, y_next, vx_next, vy_next
# Recive next position and speed
# Call with x, y, vx, vy = euler2d(x, y, vx, vy, ax, ay, step)
