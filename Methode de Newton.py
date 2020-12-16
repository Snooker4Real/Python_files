#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 13:24:23 2018

@author: jonathancindanomwamba
"""

def NewtonBis(g,gprime,x0,epsilon = 10**-15,Nmax = 400):
    xn = x0
    for k in range(Nmax):
        print(xn)
        xnp1 = xn - g(xn)/gprime(xn)
        if abs(xnp1-xn) < epsilon:
            return xnp1
        xn = xnp1
    print("Warning !! :Nmax atteint")
    return xnp1
def Derivee(f,x,h = 0.001):
    return(f(x+h) - f(x-h))/(2.*h)
def NewtonSansLaDerivee(g,x0,epsilon = 10**-15,Nmax=400):
    pass
for h in range()