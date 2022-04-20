# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:14:51 2019

@author: burak
"""
import math

th=0.01
x=1.5708
index=2
sign=-1
res=1
lastTerm=1

while math.fabs(lastTerm)>th:
    lastTerm=sign*(x**index)/math.factorial(index)
    res=res+lastTerm
    index=index+2
    sign=sign*(-1)
    