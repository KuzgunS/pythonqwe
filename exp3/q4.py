# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
import math

L1=float(input('Enter L1: '))
L2=float(input('Enter L2: '))
A=float(input('Enter A: '))
Z=float(input('Enter Z: '))

teta_1 = math.acos((L1**2 + A**2 + Z**2 - L2**2)/(2*L1*(A**2+Z**2)**0.5)) + math.atan2(Z,A)
teta_2 = math.acos((L1**2 + L2**2 - A**2 - Z**2 )/(2*L1*L2))
print("teta_1 ={:.2f} teta_2 ={:.2f} ".format(teta_1,teta_2))


