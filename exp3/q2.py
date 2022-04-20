# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
import math

x1=float(input('Enter x1: '))
x2=float(input('Enter x2: '))
w1=float(input('Enter w1: '))
w2=float(input('Enter w2: '))
b=float(input('Enter b: '))

z = x1*w1 + x2*w2 + b
y = 1/(1+math.exp(-z)) 

print("y ={:.2f}".format(y))


