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

def fusion_trie(L1,L2):
    if L1==[]:
        return L2
    elif L2==[]:
        return L1
    elif L1[0]<=L2[0]:
        return [L1[0]]+fusion_trie(L1[1:],L2)
    else:
        return [L2[0]]+fusion_trie(L1,L2[1:])
print(fusion_trie)

def tri_fusion(L): #L est à trier
    N=len(L)
    if N<=1:
        return L
    else:
        return fusion_trie(tri_fusion(L[:N//2]),trie fusion(L[N//2:]))’’