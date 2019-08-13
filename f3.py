from __future__ import division, print_function
from numpy import abs, sqrt

def regula_falsi(fun, a, b, niter=5000, ftol=1e-06, verbose=False):
    if fun(a) * fun(b) > 0:
        c = None
        msg = "The function should have a sign change in the interval."
    else:
        for cont in range(niter):
            qa = fun(a)
            qb = fun(b)
            c = (a*qb - b*qa)/(qb - qa)
            qc = fun(c)
            if verbose:
                print("n: {}, c: {}".format(cont, c))
            msg = "Maximum number of iterations reached."
            if abs(qc) < ftol:
                msg = "Root found with desired accuracy."
                break
            elif qa * qc < 0:
                b = c
            elif qb * qc < 0:
                a = c
    return c, msg

def fun(w):
    Z = 75  # impedance (ohm)
    # 1/Z = np.sqrt((1/R**2) + ((wC - (1/wL))**2))
    C = 0.6 * 1e-06  # (F)
    R = 225  # (ohm)
    L = 0.5  # (H)
    result = (sqrt((1/R**2) + ((w*C - (1/(w*L)))**2))) - (1/Z)
    return result

print(regula_falsi(fun, 1, 1000))