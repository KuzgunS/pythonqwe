# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
import math

a1=float(input('Enter a1: '))
b1=float(input('Enter b1: '))
t=float(input('Enter t: '))

A1 = math.sqrt(a1**2 + b1**2)
teta = -math.atan2(b1,a1)
g = A1*math.cos(math.pi/4*t+teta)

print("g({}) ={:.2f}".format(t,g))


