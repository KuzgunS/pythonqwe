# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
import math

px1=float(input('Enter x1: '))
py1=float(input('Enter y1: '))
pz1=float(input('Enter z1: '))

px2=float(input('Enter x2: '))
py2=float(input('Enter y2: '))
pz2=float(input('Enter z2: '))

r_outer=float(input('Enter r1: '))
r_inner=float(input('Enter r2: '))

distP1P2 = math.sqrt((px1-px2)**2 + (py1-py2)**2 + (pz1-pz2)**2)

if(distP1P2<r_outer):
    if(distP1P2<r_inner):
        print("Inner region")
    else:
        print("Outer region")
else:
    print("Not in region")

