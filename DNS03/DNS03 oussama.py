# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:45:58 2018

@author: osaad
"""

import numpy as np
import matplotlib.pyplot as plt

###############################################################################

N = 100     #Taille d'un côté du tableau
P = 10      #Taille d'un côté d'une case dans Ima (cf. fonction F1)
NbPas = 10
Tab = np.zeros((N,N))
Tabp1 = np.zeros((N,N))
"""Initialisation du motif de départ"""
Tab[50,50] = 1
Tab[50,51] = 1
Tab[51,50] = 1
Tab[51,49] = 1
Tab[52,50] = 1

###############################################################################

def F1(Tab):
    global P
    H,L = len(Tab),len(Tab[0])
    Ima = np.zeros((P*H,P*L),dtype='int')
    for j in range(H):
        for i in range(L):
            val = Tab[j,i]
            for a in range(P):
                for b in range(P):
                    Ima[P*j+b,P*i+a] = val
    return Ima

###############################################################################

def F2(Tab,Tabp1):
    H, L = len(Tab), len(Tab[0])
    for j in range(1,H-1):      #On ne traite pas les bords de l'image de 1 à H-1 exclu
        for i in range(1,L-1):
            SUM =Tab[i,j]+Tab[i-1,j-1]+Tab[i,j+1]+Tab[i,j-1]+Tab[i+1,j],Tab[i-1,j]+Tab[i-1,j+1]+Tab[i+1,j-1]
        if SUM == 3:
            Tabp1[i,j]=1
        else:
            Tabp1[i,j]=0
    Tabp1[i,j] = Tab[i,j]
    return Tabp1,Tab        #Avec l'appel de la fonction, on permute Tabp1 et Tab
                            #Tab, Tabp1 = F2(Tab,Tabp1)

###############################################################################

#La boucle for pour itérer le jeu de la vie
for k in range(NbPas):
    fig = plt.figure()
    Ima = F1(Tab)
    plt.imshow(Ima)
    _m = k//1000
    _c = (k//100)%10
    _d = (k//10)%10
    _u = k%10
    nom = "Jeu2LaVie"+str(_m)+str(_c)+str(_d)+str(_u)+".png"
    plt.savefig(nom)
    plt.close()
    print("pas :"+str(_m)+str(_c)+str(_d)+str(_u))
    Tab, Tabp1 = F2(Tab,Tabp1)
    
    
    
    