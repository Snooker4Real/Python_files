#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:11:45 2017

@author: jonathancindanomwamba
"""

import numpy as np
import random as r
import matplotlib.pyplot as plt

ListePI = []
ListeE = []
Liste2N = [10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000]
for N in Liste2N :
    X =[] #créer une liste vide
    Y = []
    # Il faut absolument initialiser
    # la liste vide avant la boucle for
    """On peut aussi commencer comme cela
    avec 3 guillets je peux passer à la ligne sans problèmes"""
    for i in range(N): # Pour générer 10 nombres aléatoires
        x = (r.random())
        x = 2*x-1
        X.append(x)
        
        y=(r.random())
        y = 2*y-1
        Y.append(y)

    #plt.plot(X,Y,'.b') # '.b' pour afficher des points bleus
    
    # On cherche maintenant le nombre de points dans le cerclede rayon 1
    
    Compteur = 0
    for i in range(N):
        xi = X[i]
        yi = Y[i]
        if xi**2 + yi**2 <=1:
            Compteur = Compteur + 1
            ListePI.append(Compteur/N*4)
            ListeE.append(np.abs(Compteur/N*4-np.pi))
            plt.plot(xi,yi,'.r')
        else:
            plt.plot(xi,yi,'.b')
    P = (Compteur * 4)/N
    print(P)