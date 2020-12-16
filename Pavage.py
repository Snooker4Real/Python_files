êt #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:07:30 2017

@author: jonathancindanomwamba
"""

import matplotlib.pyplot as plt

B1x, B1y = [], []
P = 5
for i in range(1,P) :
    B1x.append(i/P)
    B1y.append(0)

B2x, B2y = [], []
for i in range(1,P) :
    B1x.append(1)
    B1y.append(i/P)
B1y[2]=0.2
def Rotation(x,y) :
    B3x, B3y = [], []
    for i in range (len(x)):
        B3x.append(-y[i])
        B3y.append(x[i])
    return B3x, B3y

def Translation(x,y,Deltax,Deltay) :
    B3x, B3y = [], []
    for i in range (len(x)):
        B3x.append(x[i]+Deltax)
        B3y.append(y[i]+Deltay)
    return B3x, B3y

def GenereUnCarreau():
    global B1x, B1y, B2x, B2y
    B4x, B4y = Rotation(B1x,B1y)#On crée le bord gauche
    B4x.reverse()#On remet les points dans le bon ordre
    B4y.reverse()
    B3x, B3y = Translation(B2x, B2y, -1,0)
    B3x, B3y = Rotation(B3x, B3y)
    B3x, B3y = Rotation(B3x, B3y)
    B3x, B3y = Rotation(B3x, B3y)#Finalement on a tourné de -90 degrés
    B3x, B3y = Translation(B3x,B3y,0,1)
    B3x.reverse()#On admet les points dans le bon ordre
    B3y.reverse()
    X = [0]+B1x+[1]+B2x+[1]+B3x+[0]+B4x+[0]#Concaténation de liste
    Y = [0]+B1y+[0]+B2y+[1]+B3y+[1]+B4y+[0]
    return X, Y

X,Y = GenereUnCarreau()
fig = plt.figure()
plt.plot(X,Y,'b-')
plt.plot(B1x,B1y,'r*')
plt.plot(B2x,B2y,'r*')
plt.show()


