# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:19:06 2021

@author: turgut
"""

num = int(input("Enter the account number:"))

num_copy = num
digit_num = 0
while num_copy!=0:
    res = num_copy%10
    num_copy = num_copy//10
    digit_num+=1
    
num_copy = num  
check_sum = 0  
for i in range(digit_num-1,-1,-1):
    res = num_copy%10
    num_copy = num_copy//10
    if i%2!=0:
        check_sum += 2*res
    else:
        check_sum += res

if check_sum%10==0:
    print("The account number is VALID")
else:
    print("The account number is NOT valid")