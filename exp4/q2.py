# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 21:14:51 2019

@author: burak
"""

decimal=0
i=0
binary=11101

while binary!=0:
    remainder=binary%10
    binary=binary//10
    decimal=decimal+remainder*(2**i)    
    i=i+1