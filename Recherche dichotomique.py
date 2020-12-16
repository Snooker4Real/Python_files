#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 12:47:50 2018

@author: jonathancindanomwamba
"""

#La liste doit être triée par ordre croissant


def TO02(L):
    for i in range(len(L)):
        if L[i] <= L[i-1]:
            return False
        return True
def TO(L):
    L2 = L[:]
    L2.sort()
    if L2 == L:
        return True
    return False

def RDLT(L,x):
        if not TO(L):
            print("Liste non-triée")
            return   
        if x < L[0]:
            return
        if x >= L[-1]:
            return len(L)-1
#L'invariant de boucle est vérifié
        n, p = 0, len(L)-1
        while n+1 != p:
            m = (n+p)//2
            if L[m] <= x:
                n = m
        else:
            p = m
            return n
L = [1,2,5,6,7,10,15,17]
x = 5
print(RDLT(L,x))
