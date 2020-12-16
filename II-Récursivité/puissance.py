#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:40:30 2018

@author: jonathancindanomwamba
"""

def puissance(x,n):
    if n==0:
        return 1
    else :
        return x*puissance(x,n-1)

def puissance1(x,n):
    if n==0 or x==1:
        return 1
    elif n==1:
        return x
    else:
        return x*puissance1(x,n-1)

def puissance_rapide(x,n): #n \in \doubleN
    if n==0:
        return 1
    else:
        m = puissance(x,n//2)
        if n%2==0: #si n est pair
            return m*m
        else: #si n n'est oas pair, il est impair
            return x*m*m

def f(n):
    if n==0:
        return ...
    else:
        return ...f(n-1)...f(n-2)

def PGCD(a,b):
    if a%b==0:
        return b
    else:
        return PGCD(b,a%b)

L=[2,9,11,12,15,20,31,54,60]

def rech_dicho(L,x):
    n = len(L)
    if n==0:
        return False
    elif x == L[n//2]:
        return True
    else:
        if x>L[n//2]:
            return rech_dich(L[n//2+1],x)
        else:
            return rech_dicho(L[:n//2])

        
