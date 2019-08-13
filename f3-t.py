import numpy as np
import matplotlib.pyplot as plt


def FlasePosition(xl, xu, err, fnc):
    print('FlasePosition')
    xrn = 0
    i = 0
    er = err +100
    fxl = fnc(xl)
    fxu = fnc(xu)
    x = np.array([])
    y = np.array([])
    while not er <= err:
        x = np.append(x,i)
        xr = xrn
        xrn = xu - (fxu * (xl - xu))/(fxl - fxu)
        fxr = fnc(xrn)
        if not xrn == 0:
            er = np.abs((xrn - xr)/xrn) * 100
        y = np.append(y, er)
        if (fxl * fxr <0):
            xu = xrn
            fxu = fxr
        elif (fxl * fxr >0):
            xl = xrn
            fxl = fxr
        else:
            print('i = {:3d}, L = {:22}, error = {}%'.format(i,xrn,er))
            return x, y
            break
        print('i = {:3d}, L = {:22}, error = {}%'.format(i,xrn,er))
        i += 1
    return x, y


C = 1e-4
R = 280.0
t = 0.05
#q0/q(t)
qq0 = 0.01

def fncL(L):
    eP = np.exp(-(R * t/(2 * L)))
    sq = ((1/(L * C)) - ((R/(2 * L))**2))**(1/2)
    fl = eP * np.cos(sq * t) - qq0
    return fl

def dfncL(L):
    #not yet *t
    theta = np.sqrt((1/(L * C)) - (R/(2 * L))**2)
    eP = np.exp(-((R * t)/(2 * L)))
    eq1 = eP * (-(np.sin(theta * t))) * (((t/2) * ((R**2)/(2 * (L**3))) - (1/(C * (L**2))))/theta)
    eq2 = np.cos(theta * t) * eP * ((R * t)/(2 * (L**2)))
    dfL = eq1 + eq2
    return dfL

def fun(w):
    Z = 75  # impedance (ohm)
    # 1/Z = np.sqrt((1/R**2) + ((wC - (1/wL))**2))
    C = 0.6 * 1e-06  # (F)
    R = 225  # (ohm)
    L = 0.5  # (H)
    result = (np.sqrt((1/R**2) + ((w*C - (1/(w*L)))**2))) - (1/Z)
    return result

FlasePosition(1,1000,1e-06,fun)