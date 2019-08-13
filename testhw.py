import numpy as np


def f(w):
        C = 0.6 * 1e-06  # (F)
        R = 225  # (ohm)
        L = 0.5  # (H)
        result = np.sqrt((1/R**2) + ((w*C - (1/(w*L)))**2))
        result = round(result,4)
        return result


for i in range(1, 1000):
        Z = 75
        # print("%.4f" % f(i))
        if (f(i) == round(1/Z,4)):
                print("%.4f" % f(i))
                break

print("f(i)")
print("%.4f" % f(i))
print("i")
print("%d" % i)
# a = 0.123456789
# r = round(a,4)
# print(r)