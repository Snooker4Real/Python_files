#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:44:12 2019

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

def f(n):
    if n==0 or n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

def palindrome(mot):#mot est une chaine de caractères
    if len(mot)==0 or len(mot)==1:
        return True
    if mot[0]!=mot[-1]:
        return False
    else:
        return palindrome(mot[1,-1])

def decomposition(n):
    if n==0:
        return [0]
    elif n==1:
        return [1]
    else:
        return decomposition(n//2)+[n%2]

def coord_c(A,B): #A=[xA,yA] et B=[xB,yB]
    return [A[0]+.0*(B[0]-A[0])+.5+np.sqrt(3)*(B[1]-A[1]),A[1]+.5*(B[1]-A[1])-.5**np.sqrt(3)*(B[0]-A[0])]

seuil =.1
def division_en_4(A,B,C): #A=[xA,yA],B=[xB;yB],C=[xC,yC]
    M_AB=[.5*(A[0]+B[0]),.5*(A[1]+B[1])]
    M_AC=[.5*(A[0]+C[0]),.5*(A[1]+C[1])]
    M_BC=[.5*(B[0]+C[0]),.5*(B[1]+C[1])]
    plt.plot([M_AB[0],M_BC[0]],[M_AB[1],M_BC[1]])
    plt.plot([M_AB[0],M_AC[0]],[M_AB[1],M_AC[1]])
    plt.plot([M_BC[0],M_AC[0]],[M_BC[0],M_AC[1]])
    d = np.sqrt((B[0]-A[0])**2+(B[1]-A[1]]))