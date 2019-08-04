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
# print(t4)
# step_size = 2
g = 9.81  # m/s
m = 68.1  # mass (kg)
c = 12.5  # drog coefficient (kg/s)
velocity_of_the_parachutist = 0
# plt.plot(t, velocity1(t))
# plt.plot(t, velocity2(velocity1(t)))

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, sharey=True)
ax1.scatter(t2, velocity1(t2))
ax1.set_title('Diff Step = 2')
ax1.grid()
ax2.scatter(t1, velocity2(velocity1(t1), 1))
ax2.set_title('Not Diff Step = 1')
ax2.grid()
ax3.scatter(t2, velocity2(velocity1(t2), 2))
ax3.set_title('Not Diff Step = 2')
ax3.grid()
ax4.scatter(t4, velocity2(velocity1(t4), 4))
ax4.set_title('Not Diff Step = 4')
ax4.grid()

# ax5.plot(t2, velocity1(t2), label='ax1')
# ax5.plot(t1, velocity2(velocity1(t1), 1), label='ax2')
# ax5.plot(t2, velocity2(velocity1(t2), 2), label='ax3')
# ax5.plot(t4, velocity2(velocity1(t4), 4), label='ax4')
# ax5.set_title('Summary')
# ax5.grid()

# plt.xlabel('time')
# plt.ylabel('velocity')

# plt.title("terminal velocity Plot")

# plt.grid()

# plt.legend()

plt.show()
