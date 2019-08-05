import matplotlib.pyplot as plt
import numpy as np


def velocity1(t):
    # v1 = (g*m/c)*(1 - (np.exp(-(c/m)*t)))
    v1 = 53.39*(1 - np.exp(-0.18355*t))
    return v1


def velocity2(velocity, step_size):
    v2 = velocity + (g - ((c/m)*velocity))*step_size
    return v2


val_start = 0
val_stop = 16
step = 17

t   = np.linspace(val_start, val_stop, num=step)

g = 9.81  # m/s
m = 68.1  # mass (kg)
c = 12.5  # drog coefficient (kg/s)

step_size = t[1] - t[0]

print(velocity2(velocity1(t*5.5), step_size*5.5))

plt.plot(t*2, velocity1(t*2), label='diff step size = 2')
plt.plot(t*1, velocity2(velocity1(t*1), step_size*1), label='not diff step size = 1')
plt.plot(t*2, velocity2(velocity1(t*2), step_size*2), label='not diff step size = 2')
plt.plot(t*4, velocity2(velocity1(t*4), step_size*4), label='not diff step size = 4')
plt.plot(t*5, velocity2(velocity1(t*5), step_size*5), label='not diff step size = 5')
plt.plot(t*5.5, velocity2(velocity1(t*5.5), step_size*5.5), label='not diff step size = 5.5')
plt.plot(t*6, velocity2(velocity1(t*6), step_size*6), label='not diff step size = 6')
plt.plot(t*7, velocity2(velocity1(t*7), step_size*7), label='not diff step size = 7')
plt.plot(t*8, velocity2(velocity1(t*8), step_size*8), label='not diff step size = 8')
plt.plot(t*16, velocity2(velocity1(t*16), step_size*16), label='not diff step size = 16')
plt.title('Summary')

plt.grid()

plt.legend()

plt.show()
