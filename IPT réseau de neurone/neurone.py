#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 16:46:37 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt
import random as r

xi = [ 14, -1,  8,  3, -9,-24, -3,  4, 3, -17,  9,  6, 41,-16, -6, -4, -8, 19, 17, -9]
yi = [  0,  0,  0,  1,  1,  1,  1,  1, 1,   1,  0,  0,  0,  1,  1,  1,  0,  0,  0,  1]

a = 0.2
b = -0.5

def F1(x,a,b):
    return 1/(1+np.exp(a*x+b))

def F2(xi,yi,a,b):
    N = len(xi)
    S = 0
    for i in range(N):
        S = S + yi[i]*np.log(F1(xi[i],a,b))+(1-yi[i])*np.log(1-F1(xi[i],a,b))
    return -1/N*S

epsilon = 0.1
n = 100
h = .01


def F3():
    a = 0.2
    b = -0.6
    for i in range(n):
        dJ_da = (F2(xi,yi,a+h,b)-F2(xi,yi,a-h,b))/(2*h)
        dJ_db = (F2(xi,yi,a,b+h)-F2(xi,yi,a,b-h))/(2*h)
        a = a - dJ_da * epsilon
        b = b - dJ_db * epsilon
    return a, b

print("(an, bn) = ",F3())

def F31():
    
    a1, a2, a3 = X
    b1, b2, b3 = Y
"""On calcule la fonction d'évaluation en X1, X2, X3"""
    f1 = F2(xi,yi,a1,b1)
    f2 = F2(xi,yi,a2,b2)
    f3 = F2(xi,yi,a3,b3)
    """On réindixe les points pour que X1 ait la plus petite évaluation en X3"""
    L = [[f1,a1,b1],[f2,a2,b2],[f3,a3,b3]]
    L.sort()
    a1, b1 = L[0][1], L[0][2]
    a2, b2 = L[1][1], L[1][2]
    a3, b3 = L[2][1], L[2][2]
    xr = x0 +(x0-x3)
    if F2(xr) < F2(x2):
        xe = x0 +2*(x0-x3)
        if F2(xe) < f(xr):
            x3 = xe
        else :
            x3 = xr
    if F2(xr) >= F2(x2):
        xe = x3 +1/2(x0-x3)
        