#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 14:03:32 2018

@author: jonathancindanomwamba
"""

import matplotlib.pyplot as plt #présentation graphique des résultats

# Données numériques
Lambda = 1.
mu = 2.2e3
c = 800.
D = Lambda/(mu*c)
e = 30e-2
N =100
dx = e/(N-1)

dt = 5.

T0 = 20.
T1 = 30.

liste_x = []
for i in range(N):
    liste_x.append(i*dx)
#print(liste_x)

T = []
for i in range(N):
    T = [T1] + (N+1)*[T0]
#print(T)

DeltaT = N*[None]
#print(DeltaT)

for i in range(1,N-1):
    DeltaT[i] = ((D*dt)/(dx**2))*(T[i+1]+T[i-1]-2*T[i])
for i in range(1,N-1):
    T[i] += DeltaT[i]
T[N-1]=T[N-2]
#print(T)

#10 000 itérations

for iteration in range(10000):
    for i in range(1,N-1):
        DeltaT[i]=D*dt*(T[i-1]+T[i+1]-2*T[i])/dx**2
    for i in range(1,N-1):
        T[i]+=DeltaT[i]
    T[N-1]=T[N-2]
#print(T)

if iteration%500==0:
    print(T[N-1])
    plt.plot(liste_x,T)
plt.xlabel('x (m)')
plt.ylabel('T (°C)')
plt.show()

# Itérations avec condition de fon d'itérations

iteration = 0
while T[N-1]<29:
    iteration+=1
    for i in range(1,N-1):
        DeltaT[i]=D*dt*(T[i-1]+T[i+1]-2*T[i])/dx**2
    for i in range(1,N-1):
        T[i]+=DeltaT[i]
    T