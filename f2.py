from __future__ import division, print_function
from numpy import log2, ceil, abs, sqrt, array, append

def bisection(fun, a, b, c, valerr=100, xtol=1e-6, ftol=1e-06, verbose=False):
    if fun(a) * fun(b) > 0:
        c = None
        msg = "The function should have a sign change in the interval."
    else:
        nmax = int(ceil(log2((b - a)/xtol)))
        ax = array([])
        acont = array([])
        avalerr = array([])
        for cont in range(nmax):

            ax = append(ax,c)
            acont = append(acont,cont)
            avalerr = append(avalerr,valerr)

            if verbose:
                print("n: {}, x: {}, err: {}%".format(cont, c,valerr))

            valp = c
            c = 0.5*(a + b)
            valf = c
            valerr = abs((valf - valp)/valf) * 100

            if abs(fun(c)) < ftol:
                msg = "Root found with desired accuracy."
                break
            elif fun(a) * fun(c) < 0:
                b = c
            elif fun(b) * fun(c) < 0:
                a = c
            msg = "Maximum number of iterations reached."
    return ax, avalerr, acont, msg

def fun(w):
    Z = 75  # impedance (ohm)
    # 1/Z = np.sqrt((1/R**2) + ((wC - (1/wL))**2))
    C = 0.6 * 1e-06  # (F)
    R = 225  # (ohm)
    L = 0.5  # (H)
    result = sqrt((1/R**2) + ((w*C - (1/(w*L)))**2)) - (1/Z)
    return result

# print(bisection(fun, 1, 1000, 1,verbose=False))
