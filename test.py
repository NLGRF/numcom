from __future__ import division, print_function
from numpy import abs, cos, sin, exp, sqrt

C = 1e-04
R = 280.0
t = 0.05
#q0/q(t)
qq0 = 0.01
L1 = 50
theta = sqrt((1/(L1 * C)) - (R/(2 * L1))**2)
s1 = (1/(0.01 * C))
s2 = (R/(2 * 0.01))**2
print("s1 : ", s1, "\ts2", s2)
s3 = s1 - s2
print("s3 : ", s3)
print(theta)