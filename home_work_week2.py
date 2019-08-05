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
val_stop = 100
step = 101

t   = np.linspace(val_start, val_stop, num=step)
# t1  = np.linspace(0, 100, num=101)
# t2  = np.linspace(0, 100, num=51)
# t4  = np.linspace(0, 100, num=26)
# t8 = np.linspace(0, 100, num=13)
# t16 = np.linspace(0, 100, num=7)

print(t)
print(t[1] - t[0])
step_size = t[1] - t[0]
g = 9.81  # m/s
m = 68.1  # mass (kg)
c = 12.5  # drog coefficient (kg/s)
velocity_of_the_parachutist = 0
# plt.plot(t, velocity1(t))
# plt.plot(t, velocity2(velocity1(t)))

f, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(1, 6, sharey=True)
# ax1.scatter(t2, velocity1(t2))
# ax1.set_title('Diff Step = 2')
# ax1.grid()
# ax2.scatter(t1, velocity2(velocity1(t1), 1))
# ax2.set_title('Not Diff Step = 1')
# ax2.grid()
# ax3.scatter(t2, velocity2(velocity1(t2), 2))
# ax3.set_title('Not Diff Step = 2')
# ax3.grid()
# ax4.scatter(t4, velocity2(velocity1(t4), 4))
# ax4.set_title('Not Diff Step = 4')ax1.scatter(t2, velocity1(t2))
# ax1.set_title('Diff Step = 2')
# ax1.grid()
# ax2.scatter(t1, velocity2(velocity1(t1), 1))
# ax2.set_title('Not Diff Step = 1')
# ax2.grid()
# ax3.scatter(t2, velocity2(velocity1(t2), 2))
# ax3.set_title('Not Diff Step = 2')
# ax3.grid()
# ax4.scatter(t4, velocity2(velocity1(t4), 4))
# ax4.set_title('Not Diff Step = 4')
# ax4.grid()
# ax5.scatter(t8, velocity2(velocity1(t8), 8))
# ax5.set_title('Not Diff Step = 8')
# ax5.grid()
# ax6.scatter(t16, velocity2(velocity1(t16), 16))
# ax6.set_title('Not Diff Step = 16')
# ax6.grid()
# ax4.grid()
# ax5.scatter(t8, velocity2(velocity1(t8), 8))
# ax5.set_title('Not Diff Step = 8')
# ax5.grid()
# ax6.scatter(t16, velocity2(velocity1(t16), 16))
# ax6.set_title('Not Diff Step = 16')
# ax6.grid()

ax1.scatter(t*2, velocity1(t*2))
ax1.set_title('Diff Step = 2')
ax1.grid()
ax2.scatter(t, velocity2(velocity1(t), step_size))
ax2.set_title('Not Diff Step = 1')
ax2.grid()
ax3.scatter(t*2, velocity2(velocity1(t*2), step_size*2))
ax3.set_title('Not Diff Step = 2')
ax3.grid()
ax4.scatter(t*4, velocity2(velocity1(t*4), step_size*4))
ax4.set_title('Not Diff Step = 4')
ax4.grid()
ax5.scatter(t*8, velocity2(velocity1(t*8), step_size*8))
ax5.set_title('Not Diff Step = 8')
ax5.grid()
ax6.scatter(t*16, velocity2(velocity1(t*16), step_size*16))
ax6.set_title('Not Diff Step = 16')
ax6.grid()

# plt.xlabel('time')
# plt.ylabel('velocity')

# plt.title("terminal velocity Plot")

# plt.grid()

# plt.legend()

plt.show()
