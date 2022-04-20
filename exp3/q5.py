# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
import math

x1=float(input('Enter x1: '))
y1=float(input('Enter y1: '))
x2=float(input('Enter x2: '))
y2=float(input('Enter y2: '))
x3=float(input('Enter x3: '))
y3=float(input('Enter y3: '))
xq=float(input('Enter xq: '))
yq=float(input('Enter yq: '))

dist1q = math.sqrt((x1-xq)**2+(y1-yq)**2)
dist2q = math.sqrt((x2-xq)**2+(y2-yq)**2)
dist3q = math.sqrt((x3-xq)**2+(y3-yq)**2)
if(dist1q<dist2q):
    if(dist1q<dist3q):
        print("Query sample belongs to Class1")
    else:
        print("Query sample belongs to Class3")
else:
    if(dist2q<dist3q):
        print("Query sample belongs to Class2")
    else:
        print("Query sample belongs to Class3")

 

