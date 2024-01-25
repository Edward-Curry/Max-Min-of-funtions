# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:36:27 2023

@author: ecurry
"""

import numpy as np
import matplotlib.pylab as plt


q = 1.44
A = 1090
p = 0.033
x1 = 0.2
tol = 0.000000001

x = np.arange(0.2, 1., .01)

def pot(x) :
    v = A * np.exp(-x/p) - (q/x)
    return v

def forc(x) :
    f = (A/p) * np.exp(-x/p) - (q/x**2)
    return f

def forc_der(x) :
    fd = (-A/p**2) * np.exp(-x/p) + (2*q) / (x**3)
    return fd


while abs(forc(x1)) > tol :
    x1 = x1 - forc(x1) / forc_der(x1)

print("the value of x for which the potential is minimum is " , (x1))
print("the minimum potential is ", pot(x1))

plt.plot(x, forc(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("force V'(x)")
plt.savefig("force.pdf")
plt.show()

plt.plot(x, pot(x))
plt.plot (x, forc(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Potential V(x) anf Force V'(x)")
plt.savefig("potential and force.pdf")
plt.show()


