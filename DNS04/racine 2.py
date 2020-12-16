#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 20:02:48 2018

@author: jonathancindanomwamba
"""

#import numpy as np

n = int(input("n = "))
x = 1.                              #On initialise à n'iporte quelle valeur
print("x0 = ",x)
for k in range(n):
    x = (x/2.) + (1/x)
    print(x)

N = 1.                             # =/0
D = 1.                             # =/0
def f(N,D):
    for i in range(n):
        M = (N/D)**2. + 2.          #M est le numérateur à n+1
        T = 2.*(N/D)                #T est le dénomnateur à n+1
        N = M
        D = T
    return M, T
print("N, D = ",f(N,D))

M, T = f(N,D)
def g(M,T):
    X = M/T
    return X
print("Xn= ",g(M,T))
