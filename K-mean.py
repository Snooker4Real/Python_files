#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 15:36:51 2018

@author: jonathancindanomwamba
"""

import random as r
import numpy as np
import matplotlib.pyplot as plt

def InitPoints() :
    N = 300
    sigma = 1
    xA, yA = 5,5
    xB, yB = 3,1
    X, Y = [], [] # On initialise deux listes vides
    for i in range(N) :
        if r.random() < 0.5 : # On choisit au hasard si on met un point a proximité du point A ou du point B.
            x = r.gauss(xA,sigma)
            y = r.gauss(yA,sigma)
        else :
            x = r.gauss(xB,sigma)
            y = r.gauss(yB,sigma)
        X.append(x)
        Y.append(y)
    return X, Y

X, Y = InitPoints()
plt.plot(X,Y,"x")

def F1(L):
    m = L[0]
    io = 0
    for i in range(len(L)):
        if L[i] <= m:
            m= L[i]
            io = i
    return io
L = [1,2,3,4,5,0,6,7,8,9]
print("Indice du minimum = ",F1(L))

def F1v2(L):
    L2 = L[:]
    L2.sort()
    z = L2[0]
    return L.index(z)
print("indice du min : ",F1v2(L))

def F2(L):
    S = 0
    for i in range(len(L)):
        S = S + L[i]
    return S/len(L)
print("Moyenne Liste = ",F2(L))

def F3(LGx,LGy,X,Y):
    A = []
    for i in range(len(X)):
        ListeDesMiGj = []
        for j in range(len(LGx)):
            MiGj = np.sqrt((X[i]-LGx[j])**2+(Y[i]-LGy[j])**2)
            ListeDesMiGj.append(MiGj)
        # jm est l'indice du point Gj le plus proche de Mi
        jm = F1(ListeDesMiGj)
        A.append(jm)
    return A

def F4(X,Y,A,j):
    L1, L2 = [], []
    for i in range(len(A)):
        if A[i] == j:
            L1.append(X[i])
            L2.append(Y[i])
    return L1, L2

def F5(LGX,LGy,X,Y):
    A = F3(LGx,LGy,X,Y)
    LGxNext, LGyNext = [], []
    for j in range(len(LGx)):
        x, y = F4(X,Y,A,j)
        LGxNext.append(F2(x))
        LGyNext.append(F2(y))
    return LGxNext, LGyNext

X, Y = InitPoints()
LGx = [3, 2]
LGy = [5, 5]
for k in range(10):
    plt.plot(X,Y,"o")
    plt.plot(LGx,LGy,"*r")
    plt.show()
    LGx, LGy = F5(LGx,LGy,X,Y)