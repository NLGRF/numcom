from __future__ import division, print_function
from numpy import abs, cos, sin, exp, sqrt

def newton(fun, grad, x, niter=5000, ftol=1e-06, verbose=False):
    msg = "Maximum number of iterations reached."
    for cont in range(niter):
        if abs(grad(x)) < ftol:
            x = None
            msg = "Derivative near to zero."
            break
        if verbose:
            print("n: {}, x: {}".format(cont, x))
        x = x - fun(x)/grad(x)
        if abs(fun(x)) < ftol:
            msg = "Root found with desired accuracy."
            break
    return x, msg


C = 1e-04
R = 280.0
t = 0.05
#q0/q(t)
qq0 = 0.01


def fun(L):
    eP = exp(-(R * t/(2 * L)))
    sq = ((1/(L * C)) - ((R/(2 * L))**2))**(1/2)
    result1 = eP * cos(sq * t) - qq0
    return result1


def grad(L):
    #not yet *t
    theta = sqrt((1/(L * C)) - (R/(2 * L))**2)
    eP = exp(-((R * t)/(2 * L)))
    eq1 = eP * (-(sin(theta * t))) * (((t/2) * ((R**2)/(2 * (L**3))) - (1/(C * (L**2))))/theta)
    eq2 = cos(theta * t) * eP * ((R * t)/(2 * (L**2)))
    result2 = eq1 + eq2
    return result2


print(newton(fun, grad, 7))