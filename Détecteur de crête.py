#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 15:44:49 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

def f(_):
    return (10**-10)*(np.exp(_/0.025)-1)

plt.show()

def g(ucp): # ucp pour duc/dt
    global uc, v
    r, R, C =10., 10000., 10**-6
    return f(v-(R+r)/R*uc-r*C*ucp)-uc/R-C*ucp

def RD(ff,a,b,epsilon=10**-12,Nmax=2000):
    if ff(b) == 0:
        return b
    for i in range(Nmax):
        m = (a+b)/2
        if ff(m)*ff(b) <= 0 :
            a = m
        else:
            b = m
        if abs(b-a) < epsilon :
            return m
    print("Warning!")
    return m

def v2t(t):
    return (3+np.cos(2*np.pi*7*t))*np.sin(2*np.pi*200*t)

t0, t1 = 0, 0.3
N = 10000
t = np.linspace(t0,t1,N) #Liste des instants
Luc = np.zeros(N) #Liste à compléter des uc
for n in range(1,N):
    h = t[n] - t[n-1]
    uc, v = Luc[n-1], v2t(t[n-1])
    K = RD(g,-10**4,10**4)
    Luc[n] = Luc[n-1] + K * h
plt.plot(t, v2t(t),'b-')
plt.plot(t,Luc,'r-')
plt.show()