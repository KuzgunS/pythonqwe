# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:14:51 2019

@author: burak
"""
num1=25
num2=25
i=1

while i<=num1 or i<=num2:
    if (num1%i==0 and num2%i==0):
        gcd=i
    i=i+1
