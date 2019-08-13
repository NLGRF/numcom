import numpy as np
import matplotlib.pyplot as plt

# MAX_ITER = 2000


def func(R):
    return (np.exp(-0.005*R)*np.cos(np.sqrt(2000  - 0.01*(R**2)*(0.05))) - 0.01)


# Prints root of func(x) in interval [a, b]


def regulaFalsi(a, b):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result
    step = 1
    # for i in range(MAX_ITER):
    while ((b-a) >= 0.01):
        print("step: ", "%d" % step,"err: ", "%.2f" % (b-a))

        # Find the point that touches x axis
        c = (a*func(b) - b*func(a)) / (func(b) - func(a))

        # Check if the above found point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c

        step = step + 1
    
    print("Last step : ", "%d" % step)
    print("Last err : ", "%d" % (b-a))
    print("The value of root is : ", '%.4f' % c)


# Driver code to test above function
# Initial values assumed
a = -100
b = 2000
regulaFalsi(a, b)

R = np.linspace(-100, 2000, 2101)
# print(c)
# result = ((668.06/c) * (1 - np.exp(-0.146843*c))) - 40
# print(f(c))
plt.plot(R, func(R), label='Find R')

plt.grid()
plt.show()
