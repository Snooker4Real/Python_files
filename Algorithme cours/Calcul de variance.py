#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 22:39:34 2018

@author: jonathancindanomwamba
"""

def Moy(Liste):
    if not Liste:
        return
    return sum(Liste)/float(len(Liste))

def Var(Liste):
    if not Liste :
        return
    N = len(Liste)
    somme = 0.0
    moy = Moy(Liste)
    for i in range(N):
        somme = somme + (Liste[i]-moy)**2
    return somme/float(N)


L = [1,5,14,6,45,9,2]
print("Variance = ", Var(L))