#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 21:05:05 2017

@author: julia
"""
import random

def getrandom(lista):
    return random.choice(lista)

def compare(n):
    winchanging = 0
    winnotchanging = 0
    for i in range(n):
        winchanging += changing()
        winnotchanging += notchanging()
    print ("changing the door : ", winchanging/n, "\n not changing the door : ", winnotchanging/n)

def notchanging():
    prize = getrandom([1, 2, 3])
    choice = getrandom([1, 2, 3])
    if prize == choice:
        return 1
    return 0

def changing():
    prize = getrandom([1, 2, 3])
    choice = getrandom([1, 2, 3])
    if prize == choice:
        return 0
    return 1

"""
compare(5000000)
changing the door :  0.6666506 
 not changing the door :  0.3332194
 """