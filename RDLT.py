#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:14:02 2018

@author: jonathancindanomwamba
"""
def VERIF(L):
    L2=L[:]
    L2.sort()
    if L2==L:
        return True
    return False

def RDLT(L,x):
    if not VERIF(L):
        print("Liste non triée")
    N = len(L)
    if x < L[0]:
        return
    if x >= L[-1]:
        return L[-1]
    n = 0
    p = N - 1
    #L'invariant de boucle est vérifié
    while p != n+1:
        m = int((n+p)/2) #m est un entier
        if x < L[m]:
            p = m
        else:
            n = m
    return L[n] # ou n si on renvoie l'indice

#On a une liste triée dans l'ordre croissant
L = [1,3,4,5,7,10,30,35,56,90]
x = 5.5
print(RDLT(L,x)) #On appelle la fonction
