#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 15:40:52 2019

@author: jonathancindanomwamba
"""


import random as rd

L = [7,4,3,0,9,2,6,5,1,8]
def quicksort(L):
    if len(L)<=1:
        return L
    else:
        p=rd.randint(0,len(L)-1) #p est l'indice du pivot
        pluspetitquepivot=[]
        plusgrandquepivot=[]
        for i in range(len(L)):
            if i !=p: #on exclue le pivot des partitions
                if L[i]<=L[p]:
                    pluspetitquepivot.append(L[i])
                else:
                    plusgrandquepivot.append(L[i])
        return quicksort(pluspetitquepivot)+[L[p]]+quicksort(plusgrandquepivot)
print (quicksort(L))

