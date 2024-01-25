# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 11:34:23 2023

@author: ecurry
"""



import numpy as np
import matplotlib.pylab as plt
x = np.arange(-15.0, 15.0, 0.2)

a = 1
b = 0
c = -4
tol = 1
n_arr = []
tol_arr = []

while tol >  1e-10 :
    
    x1 = -5
    x2 = 0
    y3 = 1
    n_steps = 0



    tol = tol / 10
    tol_arr.append(np.log10(tol))
    while abs(y3) > tol :
         
        n_steps += 1
        
        y1 = a * x1 * x1 + b * x1 + c
        if  y1 < 0.0 :
            print("f(x1) is not greater then 0")
        
        y2 = a * x2 * x2 + b * x2 + c
        if  y2 > 0.0 :
            print("f(x3) is greater then 0")
            
        x3 = 0.5 * (x1 + x2)
        
        y3 = a * x3 * x3 + b * x3 + c
        
        if y3 > 0:
            x1 = x3
        elif y3 < 0:
            x2 = x3
        else:
            print(x3, "is the root")
    n_arr.append(n_steps)
     
print(x3, "is the approximate root")
print("it took ", n_steps, "steps to find the root")
plt.scatter(x3,y3)

plt.plot(x, a * x * x + b * x + c)
plt.plot(x, 0.0*x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Parabola")
plt.savefig("parabola p1 L.pdf")
plt.show()

print(n_arr)
print(tol_arr)
plt.plot(tol_arr,n_arr)
plt.xlabel("log(tolerance)")
plt.ylabel("number of steps")
plt.title("tolerance vs number of steps")
plt.gca().invert_xaxis()
plt.savefig("n vs tol p1.pdf")  
plt.show()
