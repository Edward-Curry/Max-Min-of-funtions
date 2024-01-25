# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:15:00 2023

@author: ecurry
"""

import numpy as np
import matplotlib.pylab as plt
x = np.arange(-15.0, 15.0, 0.2)

a = 1.0
b = 0.0
c = -4.0

n_arr = []
tol_arr = []
def parab(x) :
    result = a * x * x + b * x + c
    return result

def der_parab(x) :
    result = (2 * a) * x + b
    return result
tol = 1

while tol > 1e-10:
    x1 = -1
    n_steps = 0
    tol = tol / 10
    tol_arr.append(np.log10(tol))
    while abs(parab(x1)) > tol:
        x1 = x1 - parab(x1) / der_parab(x1)
        n_steps += 1
    n_arr.append(n_steps)
        
print ("x1 is ",x1)
print ("f(x1) is " ,parab(x1))
plt.scatter(x1, der_parab(x1))
plt.plot(x, parab(x))
plt.plot(x, der_parab(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Parabola")
plt.savefig("parabole p2 L.pdf")
plt.show()

plt.plot(tol_arr,n_arr)
plt.xlabel("log(tolerance)")
plt.ylabel("number of steps")
plt.title("tolerance vs number of steps")
plt.scatter(-1,40, color = "white")

plt.gca().invert_xaxis()
plt.savefig("n vs tol p2.pdf")

plt.show()