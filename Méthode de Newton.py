#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:44:59 2018

@author: jonathancindanomwamba
"""

import matplotlib.pyplot as plt
import numpy as np

def Derivee(f, x, h = 10**-5):
    return (f(x+h)-f(x-h))/2/h
def NewtonBis(f, x0, epsilon = 10**-15, Nmax = 400, h = 10**-5):
    xn = x0
    for i in range(Nmax):
        print(xn)
        xnp1 = xn - f(xn)/Derivee(f,xn,h)
        if abs(xnp1-xn) < epsilon:
            return xnp1
        xn = xnp1
    print("Warning")
    return xnp1

print(NewtonBis(np.sin,3.))
