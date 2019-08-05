import numpy as np


def func(c):
    return ((668.06/c) * (1 - np.exp(-0.146843*c))) - 40


# Prints root of func(x)
# with error of EPSILON


def bisection(a, b):

    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    step = 1
    while ((b-a) >= 0.01):
        print("step: ", "%d" % step,"err: ", "%.2f" % (b-a))
        # Find middle point
        c = (a+b)/2

        # Check if middle point is root
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
    print("The value of root is : ", "%.4f" % c)


# Driver code
# Initial values assumed
a = -200
b = 300
bisection(a, b)

# This code is contributed
# by Anant Agarwal.
