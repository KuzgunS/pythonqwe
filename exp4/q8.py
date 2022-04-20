# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:55:39 2021

@author: turgut
"""

num = int(input("Enter the number:"))
n=0
copy_num = num
while num!=0:
    num=num//10
    n+=1
print("Digit number is {}".format(n))
if n%2==1:
    i=0
    left_sum=0
    right_sum=0
    num=copy_num
    while i<n:
        rem=num%10
        num=num//10
        if(i<n/2):
            right_sum+=rem
        if(i>n/2):
            left_sum+=rem
        i+=1
    if left_sum==right_sum:
        print("X Number")
    else:
        print("Not X Number")
else:
    print("Not X Number")