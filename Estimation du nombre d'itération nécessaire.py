#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 12:44:22 2017

@author: jonathancindanomwamba
"""

import numpy as np

def f(x):
        return x**2 - 2

def RD(f,a,b,epsilon=10**-16,Nmax=400):
    if f(a) == 0:
        return a
    for i in range(Nmax):
        m=(a+b)/2
        if f(a)*f(m)<=0:
            b=m
        else:
            a=m
        if (b-a)<epsilon:
            return m
    print("Attention : Nmax atteint !")
    return m #on renvoie tout de même le résultat
print(RD(np.sin,3,4,10**-50))