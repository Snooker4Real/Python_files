#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:20:00 2018

@author: jonathancindanomwamba
"""

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
    _ = (MAz + (xA - x)*RAy - (yA - y)*RAx)/E/I
    xpp = yp*_
    ypp = -xp*_
    """On renvoie un tableau"""
    return np.array([xp, yp, xpp, ypp])

def Eval():
    global E, I, xA, yA, xB, yB, Teta0, N, L, MAz, RAx, RAy
    s = np.linspace(0,L,N)
    RAy = MAz/xB    #cf. énoncé
    """Initialisation des listes Lx, Ly : Trajectoire de la poutre"""
    Lx = []
    Ly = []
    """ Résolution """
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
    return np.array([Lx[-1]-xB,         Ly[-1]-yB])

def Gradient():
    global E, I, xA, yA, xB, yB, Teta0, N, L, MAz, RAx, RAy
    h = 0.0001
    """ Dérivée partielle par rapport à MAz"""
    MAz = MAz + h       #Pour calculer MAz + h
    a, b = Eval()
    MAz = MAz - 2*h     #Pour calculer MAz_initial - h
    c, d = Eval()
    MAz = MAz + h
    dEval_x_Sur_dMAz = (a-c)/2/h
    dEval_y_Sur_dMaz = (b-d)/2/h
    """ Dérivée partielle par rapport à Teta0"""
    Teta0 = Teta0 + h
    a, b = Eval()
    Teta0 =Teta0 - 2*h
    c, d = Eval()
    Teta0 = Teta0 + h
    dEval_x_Sur_dTeta0 = (a-c)/2/h
    dEval_y_Sur_dTeta0 = (b-d)/2/h
    Grad = np.array([[dEval_x_Sur_dMAz,dEval_x_Sur_dTeta0], [dEval_y_Sur_dMaz,dEval_y_Sur_dTeta0]])
    return Grad
""" DONNEES """
E = 1
I = 1
xA = 0.
yA = 0.
xB = 0.8
yB = 0
Teta0 = 0.3
L = 1.
N = 1000
s = np.linspace(0,L,N)
MAz = 2
RAx = 1
RAy = MAz/xB#cf. énoncé
"""Début méthode de Newton"""
for i in range(10):
    Ev = Eval()
    Gr = Gradient()
    a, b = np.linalg.solve(Gr,-Ev)
    MAz = MAz + a
    Teta0 = Teta0 + b
    print(MAz, Teta0, Ev)

"""Fin méthode de Newton 2D"""

"""Initialisation des listes LX, LY :trajectoire de la poutre"""
Lx = []
Ly = []

"""Résolution"""
X = np.array([xA, yA, np.cos(Teta0), np.sin(Teta0)]) #CI
for n in range(1,N):
    h = s[n]-s[n-1]
    K1 = F(X)
    K2 = F(X+K1*h/2)
    K3 = F(X+K2*h/2)
    K4 = F(X+K3*h)
    X = X + (K1 + 2*K2 + 2*K3 + K4)/6*h
    Lx.append(X[0])
    Ly.append(X[1])
""" Tracé de la courbe """
print(Eval())
fig = plt.figure()
plt.plot(Lx,Ly)
plt.show()
    