#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 15:44:26 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

t, v1, v2 = [], [], []

with open("IPT_AcquisitionIndexa.txt","r") as Filename:
    Filename.readline() #lecture de la première ligne
    while 1:
        a = Filename.readline()
        if not a :
            break
        a = a.replace(",",".")
        b = a.split()
        c = float(b[0])
        t.append(c)
        d = float(b[1])
        v1.append(d)
        e = float(b[2])
        v2.append(e)
fig = plt.figure()
plt.plot(t,v2)
plt.show()

def NDer(t,v2):
    h = 0.02
    dv2_dt1=(1/h)((-3/2)*v2[0]+2*v2[1]-0.5*v2[2])
    dv2_dt0 = (1/h)*(0.5*v2[len(v2)-3]-2*v2[len(v2)-2]+1.5*v2[len(v2)-1])
    for n in range(len(v2)):
        a2 = (v2[n+1]-v2[n-1])*(1/2*h)
    return a2
fig = plt.figure()
plt.subplot(211)
plt.plot(t,v2)
plt.ylabel("W plateau (rad/s)")
plt.subplot(212)
plt.plot(t,a2)
plt.xlabel("t(s)")
plt.ylabel("dW/dt plateau (rad/s**2)")
plt.show()