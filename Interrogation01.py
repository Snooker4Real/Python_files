#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:34:44 2018

@author: jonathancindanomwamba
"""

import numpy as np
#import matplotlib.pyplot as plt

#def f(x):
#    y=np.sin(x)
#    return y
#    
#x=np.linspace(-3.,5.,100)
#y=f(x)

#plt.plot(x,y)
#plt.show()



###############################################################################

#N = 10
#def IR(f,a,b,N):
#    epsilon = (b-a)/N
#    S = 0 # Initialisation
#    for i in range(1,N):
#        xi = a + epsilon * i
#        S = S + f(xi)
#    S = epsilon/2*(f(a)+2*S+f(b))
#    return S
#print(IR(np.sin,0,np.pi/2,N))
#a = 0
#b = pi/2
###############################################################################
N = 100
def IT(f,a,b,N):
    epsilon = (b-a)/N
    S = 0 # Initialisation
    for i in range(1,N):
        xi = a + epsilon * i
        S = S + f(xi)
    S = f(xi)
    return S
print(IT(np.sin,0,np.pi/2,N))
###############################################################################
N=100
def I(f, a, b, N):
    I = ((4*IT(f,a,b,2*N)-IT(f,a,b,N))/3)
    return I
print(I(np.sin, 0, np.pi/2, N))
