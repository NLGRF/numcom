import numpy as np
import matplotlib.pyplot as plt


def func(R):
    return np.exp(-0.005*R)*np.cos(np.sqrt(2000  - 0.01*(R**2)*(0.05))) - 0.01

# Derivative of the above function
# which is 3*x^x - 2*x


def derivFunc(x):
    return 3 * x * x - 2 * x

# Function to find the root


def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print("The value of the root is : ", "%.4f" % x)


# Driver program to test above
x0 = -20  # Initial values assumed
newtonRaphson(x0)
