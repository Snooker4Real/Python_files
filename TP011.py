# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:52:08 2017

@author: admin
"""

import numpy as np
import matplotlib.pyplot as plt
import random as r

Liste2N = [10,20,30,40,50,60,70,80,90,
           100,200,300,400,500,600,700,800,900,
           1000,2000,3000,4000,5000,6000,7000,8000,9000,
           10000,20000,30000,40000,50000,60000,70000,80000,90000,
           100000,200000,500000,1000000]
ListePI = []
ListeErreur = []
for N in Liste2N :
    X = [] # On initialise une liste vide
    Y = []
    for i in range(N) :
        x = r.random()
        x = 2*x-1
        X.append(x)
        y = r.random()
        y = 2*y-1
        Y.append(y)
    Compteur = 0
    for i in range(N) :
        xi = X[i]
        yi = Y[i]
        if xi**2+yi**2 <= 1 :
            Compteur = Compteur + 1
    print("Avec N=",N," pi environ égal à ",Compteur/N*4)
    ListeErreur.append(  np.abs(Compteur/N*4-np.pi)  )
    ListePI.append(Compteur/N*4)
plt.plot(Liste2N,ListeErreur,'or')
plt.xscale('log')
plt.yscale('log')
plt.show()
    












