#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:22:39 2017

@author: jonathancindanomwamba
"""

import matplotlib.pyplot as plt 

xB1, yB1 = [], []
P = 5
for i in range(1,P): 
    xB1.append(i/P)
    yB1.append(0)
print("xB1=",xB1,"\nyB1=",yB1)

xB2, yB2 = [], []
    for i in range(1,P): 
        xB2.append(1)
        yB2.append(i/P)
print("xB2=",xB2,"\nyB2=",yB2)

fig = plt.figure() 
plt.plot(xB1,yB1,"r-")
plt.plot(xB1,yB1,"r*")
plt.plot(xB2,yB2,"r-")
plt.plot(xB2,yB2,"r*") 
plt.show()

def Rotation(x,y): 
    xB3, yB3 = [], []
for i in range (len(x)) : 
    xB3.append(-y[i])
    yB3.append(x[i])
return xB3, yB3

def Translation(x,y,Deltax,Deltay): 
    xB4, yB4 = [], []
for i in range (len(x)) : 
    xB4.append(x[i]+Deltax)
    yB4.append(y[i]+Deltay)
return xB4, yB4

def GenereUnCarreau() :
    global xB1, yB1, xB2, yB2 
    xB4, yB4 = Rotation(xB1,yB1) # On crée le bord de gauche 
    xB4.reverse() #On remet les points dans le bon ordre
    yB4.reverse()
xB3, yB3 = Translation(xB2, yB2,-1,0)
xB3, yB3 = Rotation(xB3,yB3)
xB3, yB3 = Rotation(xB3,yB3)
xB3, yB3 = Rotation(xB3,yB3) #Finalement on a tourné de -90 degrés
xB3, yB3 = Translation(xB3,yB3,0,1)
xB3.reverse() #On remet les points dans le bon ordre
yB3.reverse()
X = [0.]+xB1+[1.]+xB2+[1.]+xB3+[0.]+xB4+[0.] # Concaténation de liste
Y = [0.]+yB1+[0.]+yB2+[1.]+yB3+[1.]+yB4+[0.] #idem
return X, Y

#Création des 3 nouveaux carreaux
X,Y = GenereUnCarreau()
X1, Y1 = Rotation(X,Y)
X2, Y2 = Rotation(X1,Y1)
X3, Y3 = Rotation(X2,Y2)
L2Cx = [X,X1,X2,X3]
L2Cy = [Y,Y1,Y2,Y3]

K = len(L2Cx) # Nombre de carreaux vaut 4 à ce moment du code 
for i in range(K):
    Xep, Yep = Translation(L2Cx[i],L2Cy[i],0,2) #on déplace de 0 2 les carreaux 
    L2Cx.append(Xep)
    L2Cy.append(Yep)
    Xep, Yep = Translation(L2Cx[i],L2Cy[i],2,0)
    L2Cx.append(Xep)
    L2Cy.append(Yep)
    Xep, Yep = Translation(L2Cx[i],L2Cy[i],2,2)
    L2Cx.append(Xep)
    L2Cy.append(Yep)

fig = plt.figure()
for i in range(len(L2Cx)): 
    plt.plot(L2Cx[i],L2Cy[i],'b-') #Affichage des i carreaux
    plt.plot(xB1,yB1,'r*')
    plt.plot(xB2,yB2,'r*')
    plt.show()