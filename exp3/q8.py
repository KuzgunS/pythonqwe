# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:53:00 2021

@author: turgut
"""
goal=float(input('Enter goal: '))
dist=float(input('Enter dist: '))

if(goal==1):    
    if(dist>=16.5):
        print("He scores, absolutely brilliant!")
    else:
        if(dist>5.5):
            print("A fantasctic move and a good finish!")
        else:
            print("He finds the net with ease")
else:
    print("He should have scored")


