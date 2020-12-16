#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:48:47 2018

@author: jonathancindanomwamba
"""
import numpy as np

def NextStep(x):
    E = 0
    while not x < 10: #ou while x >= 10
        x = x / 10
        E = E + 1
    return x, E #x est la mantisse

def LOG(x,Nb=15):
    if x <= 0:
        return
    if x < 1:
        return -LOG(1/x,Nb) #x vérifie x >= #
    
    M, E = NextStep(x)
    R = str(E) + "."
    for i in range(Nb):
        M, E = NextStep(M**10)
        R = R + str(E)
    return float(R)
print(LOG(123))
print(np.log10(123))