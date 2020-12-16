t#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 21:01:21 2018

@author: jonathancindanomwamba
"""

def Max(L):
    N = len(L)
    max = L[0]
    i0 = 0
    for i in range(N):
        if L[i] > max :
            i0 = i
            max = L[i]
    return i0

L = [1,2,3,4,5,6,7,80,45,9,0,10]
c = Max(L)
print("Maximum = ",L[c])

#On ne parcours la liste qu'une seule fois, la complexité est donc T = O(N)