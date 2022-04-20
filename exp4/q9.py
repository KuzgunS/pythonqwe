# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:04:55 2021

@author: turgut
"""

#%% 
import math

a = int(input("Enter first boundary:"))
b = int(input("Enter second boundary:"))
tol = float(input("Enter tolerance:"))

def f(x):
    return x**2-4

c = b - f(b)*((b-a)/(f(b)-f(a)))
while math.fabs(f(c))>tol:  
    if f(a)*f(c)<0:
        b = c
    else:
        a = c
    print("New interval a {:.2f} and b {:.2f}".format(a,b))
    c = b - f(b)*((b-a)/(f(b)-f(a)))      
print("Root {:.2f}".format(c))
print("Function predicted result {:.2f}".format(f(c)))
print("Function exact result {:.2f}".format(f(2.8552)))



# %%
