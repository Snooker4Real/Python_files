#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:55:19 2018

@author: jonathancindanomwamba
"""


"------1------"
def Moy(Liste):
    if not Liste :
        return
    N = len(Liste)
    somme = 0.
    for i in range(N):
        somme = somme +Liste[i]
    return somme/N


L = [1,2,3,498,99,6,7,8,45,9]
print("Moyenne1 = ", Moy(L))

"------2------"
def Moy2(Liste):
    if not Liste:
        return
    somme = 0.
    for i in Liste :
        somme = somme + i
    return somme/len(Liste)

print ("Moyenne2 = ", Moy2(L))

"------3------"
def Moy3(Liste):
    if not Liste:
        return
    return sum(Liste)/float(len(Liste))

print("Moyenne3 = ", Moy3(L))