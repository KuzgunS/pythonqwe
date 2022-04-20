# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:26:26 2021

@author: turgut
"""

num = int(input("Enter the number:"))

num_copy = num
narcissistic_num = 0
while num_copy!=0:
    res = num_copy%10
    num_copy = num_copy//10
    narcissistic_num += res**4

if narcissistic_num == num:
    print("The account number is NARCISSISTIC")
else:
    print("The account number is NOT narcissistic")