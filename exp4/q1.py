# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:14:51 2019

@author: burak
"""
import math

sum=0
x=2
for n in range(1,8):
    if n%2==1:
        sum=sum+(x**n)/math.factorial(n)
       
    