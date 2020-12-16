#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:08:46 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

def F(X):
    global RAx, RAy, MAz, E, I, xA, yA
    x, y, xp, yp, = X
    xpp = yp *(MAz + (xA - x)*RAy - (yA - y)/E/I)
    ypp = -xp*(MAz + (xA - x)*RAy - (yA - y)/E/I)
    return np.array([xp, yp, xpp, ypp])
""" DONNEES """

xA = 0.
yA = 0.
xB = 0.8
yB = 0
E = 1
I = 1
MAz = 2
RAx = 1
RAy = MAz/xB
L = 1
N = 1000
Teta0 = 0

Lx = []
Ly = []
""" Résolution """
s = np.linspace(0,L,N)
X = np.array([xA,yA,np.cos(Teta0),np.sin(Teta0)])
for n in range(1,N):
    h = s[n] - s[n-1]
    K1 = F(X) 
    K2 = F(X+K1*h/2)
    K3 = F(X+K2*h/2)
    K4 = F(X+K3*h)
    X = X + (K1 +2*K2 + 2*K3 + K4)/6*h
    Lx.append(X[0])
    Ly.append(X[1])
""" Affichage de la déformée de la poutre """
fig = plt.figure()
plt.plot(Lx,Ly)
plt.show()
    