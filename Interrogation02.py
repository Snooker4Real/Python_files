#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:35:31 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

#h = 1
#x = np.linspace(-5,5,2000)
#def F1(f,x,h):
#    return (f(x+h)-f(x))/h 
#plt.plot(x,F1(f,x,h))
###############################################################################
#def f(x):
#    return np.cos(x)
#x = np.linspace(-5, 5,2000)

#plt.plot(x,f(x))
###############################################################################
x = 1
y = np.cos(1)
h = 10**-6
Z = np.cos(1+h)
E1 = np.abs(((Z-y)/h)+(np.sin(x)))
print("E1 =",E1)

h = 10**-5
Z = np.cos(1+h)
E2 = np.abs(((Z-y)/h)+(np.sin(x)))
print("E2 =",E2)

h = 10**-4
Z = np.cos(1+h)
E3 = np.abs(((Z-y)/h)+(np.sin(x)))
print("E3 =",E3)

h = 10**-3
Z = np.cos(1+h)
E4 = np.abs(((Z-y)/h)+(np.sin(x)))
print("E4 =",E4)

h = 10**-2
Z = np.cos(1+h)
E5 = np.abs(((Z-y)/h)+(np.sin(x)))
print("E5 =",E5)

h = 10**-1
Z = np.cos(1+h)
E6 = np.abs(((Z-y)/h)+(np.sin(x)))
print("E6 =",E6)
###############################################################################
Erreur = np.log([E6, E5, E4, E3, E2, E1])
h1 = np.log([10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1])
print("Erreur=",Erreur)
print("h1=",h1)
def A(X,Y):
    return
X = np.linspace(min(h1),max(h1),10)
Y = np.linspace(min(Erreur),max(Erreur),10)
plt.plot(X,Y,"*y")
P = (np.log(E6)-np.log(E5))/(np.log(10**-6)-np.log(10**-5))
print("Pente=",P)
###############################################################################
#h = 1
#x = np.linspace(-5,5,2000)
#def F2(f,x,h):
#    return (f(x+h)-f(x-h))/2*h 
#plt.plot(x,F2(f,x,h))
###############################################################################
#x = 1
#h = 10**-6
#y = np.cos(1-h)
#Z = np.cos(1+h)
#E1 = np.abs(((Z-y)/2*h)+(np.sin(x)))
#print("E1 =",E1)

#h = 10**-5
#y = np.cos(1-h)
#Z = np.cos(1+h)
#E2 = np.abs(((Z-y)/2*h)+(np.sin(x)))
#print("E2 =",E2)

#h = 10**-4
#y = np.cos(1-h)
#Z = np.cos(1+h)
#E3 = np.abs(((Z-y)/2*h)+(np.sin(x)))
#print("E3 =",E3)

#h = 10**-3
#y = np.cos(1-h)
#Z = np.cos(1+h)
#E4 = np.abs(((Z-y)/2*h)+(np.sin(x)))
#print("E4 =",E4)

#h = 10**-2
#y = np.cos(1-h)
#Z = np.cos(1+h)
#E5 = np.abs(((Z-y)/2*h)+(np.sin(x)))
#print("E5 =",E5)

#h = 10**-1
#y = np.cos(1-h)
#Z = np.cos(1+h)
#E6 = np.abs(((Z-y)/2*h)+(np.sin(x)))
#print("E6 =",E6)
###############################################################################
#Erreur = np.log([E6, E5, E4, E3, E2, E1])
#h1 = np.log([10**-6, 10**-5, 10**-4, 10**-3, 10**-2, 10**-1])
#print("Erreur=",Erreur)
#print("h1=",h1)