#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:21:11 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

def F(x,t):
    x, xp = X
    xpp = -wO**2*x - w0/Q*xp
    Xp = np.array([xp,xpp])
    return Xp

w0 = 10.
Q = 1.
X = np.array([1.,0.])
N = 1000
t0, t1 = 0., 10.
t = np.linspace(t0,t1,N)
Lx = np.zeros(N)    #séquence pour x
Lxp = np.zeros(N)   #séquence pour xp
Lx[0],Lxp[0] = X    #CI
for i in range(N):
    h = t[n] - t[n-1]
    X  = X +F(x,t[n-1])*h
    Lx[n] = X[0]
    Lxp[n] = X[1]
    
fig = plt.fig() #Chronogramme
plt.plot(t,Lx)
plt.show()
fig = plt.figure()#Portrait de phase
plt.plot()
plt.show()