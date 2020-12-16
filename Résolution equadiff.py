#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:52:52 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,t):
    return x

t0, t1 = 0, 5
N = 10
t = np.linspace(t0,t1,N)
x0 = 1 #C.I
xn = x0 #On initialise x avec la CI




Lx =np.zeros(N)
Lx = [x0]
for n in range(1,N):
#    xn = xn+f(xn,t[n-1])*(t[n]-t[n-1])
    h = t[n]-t[n-1]
    K1 = f(xn,t[n-1])
    K2 = f(xn+K1*h,t[n])
    xn = xn +(K1+K2)/2*h
    Lx[n] = xn
print(xn-np.exp(t1))
fig = plt.figure()
plt.plot(t,Lx,'*r')
plt.xlabel("t")
plt.ylabel("x")
plt.show()
