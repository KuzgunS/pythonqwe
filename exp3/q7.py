# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
import math

s_open=float(input('Enter open score: '))
s_close=float(input('Enter close score: '))
s_semi_open=float(input('Enter semi-open score: '))

p_open = math.exp(s_open)/ (math.exp(s_open) + math.exp(s_close) +math.exp(s_semi_open))
p_close = math.exp(s_close)/ (math.exp(s_open) + math.exp(s_close) +math.exp(s_semi_open))
p_semi_open = math.exp(s_semi_open)/ (math.exp(s_open) + math.exp(s_close) +math.exp(s_semi_open))

if(p_open>p_close):    
    if(p_open>p_semi_open):
        print("Open door")
    else:
        print("Semi-Open door")
else:
    if(p_close>p_semi_open):
        print("Close door")
    else:
        print("Semi-Open door")


