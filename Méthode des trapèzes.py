#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:14:16 2017

@author: jonathancindanomwamba
"""
import numpy as np

def IT(f,a,b,N):
    epsilon = (b-a)/N
    S = 0 # Initialisation
    for i in range(1,N):
        xi = a + epsilon * i
        S = S + f(xi)
    S = espislon/2*(f(a)+2*S+f(b))
    return S
print(IT(np.sin,0,np.pi/2,N))
# a = 0 et b = pi/2