# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:02:44 2021

@author: turgut
"""

num = int(input("Enter the number to check automorphic:"))

multip = num*num
num_copy = num
digit_num = 0
while num_copy!=0:
    res = num_copy%10
    num_copy = num_copy//10
    digit_num+=1
 
pseudo_num = 0
for i in range(digit_num):
    pseudo_num += (multip%10)*(10**i)
    multip = multip//10
        
if pseudo_num==num:
    print("The number is automorphic")
else:
    print("The number is NOT automorphic")