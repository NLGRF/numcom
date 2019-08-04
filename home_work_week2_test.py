import matplotlib.pyplot as plt
import numpy as np


def velocity1(t):
    # v1 = (g*m/c)*(1 - (np.exp(-(c/m)*t)))
    v1 = 53.39*(1 - np.exp(-0.18355*t))
    return v1


def velocity2(velocity, step_size):
    v2 = velocity + (g - ((c/m)*velocity))*step_size
    return v2


t1 = np.linspace(0, 100, num=101)
t2 = np.linspace(0, 100, num=51)
t4 = np.linspace(0, 100, num=26)

g = 9.81  # m/s
m = 68.1  # mass (kg)
c = 12.5  # drog coefficient (kg/s)

plt.plot(t2, velocity1(t2), label='ax1')
plt.plot(t1, velocity2(velocity1(t1), 1), label='ax2')
plt.plot(t2, velocity2(velocity1(t2), 2), label='ax3')
plt.plot(t4, velocity2(velocity1(t4), 4), label='ax4')
plt.title('Summary')

plt.grid()

plt.legend()

plt.show()
