#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 16:11:38 2018

@author: jonathancindanomwamba
"""

import numpy as np
import mpl_toolkits.mplot3d as axes3d
import matplotlib.pyplot as plt

def PV(xA,yA,zA,xB,yB,zB):
    return np.array([yA*zB-zA*yB,
              zA*xB-xA*zB,
              xA*yB-yA*xB])
def dB(xP0,yP0,zP0,xP1,yP1,zP1,xM,yM,zM,I):
    A = PV(xP1-xP0,yP1-yP0,zP1-zP0,xM-xP0,yM-yP0,zM-zP0)
    PM = np.sqrt((xM-xP0)**2+(yM-yP0)**2+(zM-zP0)**2)
    return I*A/PM**3

def B(LxP,LyP,LzP,xM,yM,zM,I):
    N = len(LxP)
    Btotal = ""
    for i in range(N-1):
        xP0, yP0, zP0 = LxP[i],LyP[i],LzP[i]
        xP1, yP1, zP1 = LxP[i+1],LyP[i+1],LzP[i+1]
        Btotal = Btotal + dB(xP0,yP0,zP0,xP1,yP1,zP1,xM,yM,zM,I)
    return Btotal

def F(X,s):
    global LxP, LyP, LzP, I
    xM, yM, zM = X
    Btot = B(LxP,LyP,LzP,xM,yM)
    NormeBtot = np.sqrt((Btot[0])**2+(Btot[1])**2+(Btot[2])**2)
    return Btot/NormeBtot

"""Construcion du fil"""
Teta = np.linspace(0,2*np.pi,500)
LxP = 10*np.cos(Teta)
LyP = 10*np.sin(Teta)
LzP = Teta*0

N = 5000
I = 1
s = np.linspace(0,500,N)
X = np.array([3.,3.,0.])
LxM, LyM, LzM = [], [], []
for n in range(1,N):
    h = s[n] - s[n-1]
    #Euler
    
    K1 = F(X       ,s[n-1]    )
    K2 = F(X+K1*h/2,s[n-1]+h/2)
    K3 = F(X+K2*h/2,s[n-1]+h/2)
    K4 = F(X+K1*h  ,s[n-1]+h  )
    X = X +(K1+2*K2+2*K3+K4)/6*h
    LxM.append(X[0])
    LyM.append(X[1])
    LzM.append(X[2])
    
fig =plt.figure()
ax = plt.gca(proection='3d')
ax.plot(LxP,LyP,LzP,'r')
ax.plot(LxM,LyM,LzM,'b')
plt.show()