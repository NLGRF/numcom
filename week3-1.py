import matplotlib.pyplot as plt
import numpy as np

def f(c):
    result = ((668.06/c) * (1 - np.exp(-0.146843*c))) - 40
    return result


c = np.linspace(1, 100, 100)
# print(c)
# result = ((668.06/c) * (1 - np.exp(-0.146843*c))) - 40
# print(f(c))
plt.plot(c, f(c), label='Find C')

plt.grid()
plt.show()