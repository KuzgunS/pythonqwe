# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
import math

x0=float(input('Enter x0: '))
y0=float(input('Enter y0: '))
q0=float(input('Enter q0 in degree: '))
r=float(input('Enter r: '))
w=float(input('Enter w: '))
t=float(input('Enter t: '))

rad = math.radians(q0)
x = x0 - r*math.sin(rad) + r*math.sin(rad + w*t)
y = y0 + r*math.cos(rad) - r*math.cos(rad + w*t)
q = q0 + w*t
print("x ={:.2f} y ={:.2f} teta ={:.2f}".format(x,y,q))


