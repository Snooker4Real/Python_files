#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:28:43 2018

@author: jonathancindanomwamba
"""
L = [7,4,8,9,3,0,1,6,2,5]
def tri_insertion(L): #L à trier
    N = len(L)
    for i in range(1,N):
        j = i
        while j>0 and L[j]<L[j-1]:
            tmp = L[j]
            L[j]=L[j-1]
            L[j-1]=tmp
            j = j-1
    return L

def tri_insertion_mieux(L):
    N = len(L)
    for i in range(1,N):
        x = L[i]
        j = i
        while j>0 and x<L[j-1]:
            l[j]=L[j-1]
            j = j-1
        L[j]=x
    return L