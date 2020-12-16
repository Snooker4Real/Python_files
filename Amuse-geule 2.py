#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:14:08 2017

@author: jonathancindanomwamba
"""

L = [3,2]
R = [0,0,0,0,0]

def f2(L):
    N = len(L)
    a=0
    for i in range(N):
        print(L[i])
        a = L[i]
        R[a] = 1
    return R

print(f2(L))
    