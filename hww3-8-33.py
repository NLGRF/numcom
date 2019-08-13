import numpy as np
import matplotlib.pyplot as plt


def func(w):
    Z = 75  # impedance (ohm)
    # 1/Z = np.sqrt((1/R**2) + ((wC - (1/wL))**2))
    C = 0.6 * 1e-06  # (F)
    R = 225  # (ohm)
    L = 0.5  # (H)
    result = np.sqrt((1/R**2) + ((w*C - (1/(w*L)))**2)) - (1/Z)
    # result = round(result,4)
    return result


# Prints root of func(x)
# with error of EPSILON


def bisection(a, b):

    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return -1

    c = a
    step = 1
    x = np.array([])
    y = np.array([])
    # Error = (b-a)
    while ((b-a) >= 0.01):
        x = np.append(x,step)
        y = np.append(y,(b-a))
        # print("step: ", "%d" % step, "err: ", "%.2f" % (b-a))
        # Find middle point
        c = (a+b)/2
        print("step: ", "%d" % step, "\terr: ", "%.2f" % (b-a), "\tc: ", "%.2f" % c)
        # Check if middle point is root
        if (func(c) == 0.0):
            # print("---")
            # print(func(c))
            # print("---")
            break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
        # elif(func(c) * func(a) < 0):
            b = c
        else:
            a = c

        step = step + 1
    print("Last step : ", "%d" % step)
    print("Last err : ", "%d" % (b-a))
    print("The value of root is : ", "%.4f" % c)
    return x, y


# Driver code
# Initial values assumed
a = 1
b = 1000
bisection(a, b)

# MAX_ITER = 1000


# Prints root of func(x) in interval [a, b]


def regulaFalsi(a, b):

    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b")
        return -1

    c = a  # Initialize result
    step = 1
    x = np.array([])
    y = np.array([])
    # for i in range(MAX_ITER):
    while((b-a) >= 0.01):
        x = np.append(x,step)
        y = np.append(y,(b-a))
        print("step: ", "%d" % step, "err: ", "%.2f" % (b-a))
        # Find the point that touches x axis
        c = ((a * func(b)) - (b * func(a))) / (func(b) - func(a))

        # Check if the above found point is root
        if (func(c) == 0):
            break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
        # elif(func(c) * func(a) < 0):
            b = c
        else:
            a = c

        step = step + 1
        
    print("Last step : ", "%d" % step)
    print("Last err : ", "%d" % (b-a))
    print("The value of root is : ", "%.4f" % c)
    return x, y


# Driver code to test above function
# Initial values assumed
a = 1
b = 1000
# regulaFalsi(a, b)


# w = np.linspace(1, 1000, 1101)
# # print(w)
# plt.plot(w, func(w), label='Find w')
x1, y1 = bisection(a, b)
# x2, y2 = regulaFalsi(a, b)
plt.plot(x1, y1, label='Find w : bisection()')
# plt.plot(x2, y2, label='Find w : regulaFalsi()')

plt.legend()
plt.grid()
plt.show()
