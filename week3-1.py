import matplotlib.pyplot as plt
import numpy as np

def f(c):
    C = 0.6 * 1e-06 # (F)
    R = 225 # (ohm)
    L = 0.5 # (H)
    result = np.sqrt((1/R**2) + ((w*C - (1/(w*L)))**2))
    return result


w = np.linspace(1, 1000, 1101)
print(w)
# result = ((668.06/c) * (1 - np.exp(-0.146843*c))) - 40
# print(f(c))
plt.plot(w, f(w), label='Find w')

plt.grid()
plt.show()