#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:57:01 2017

@author: jonathancindanomwamba
"""

L = [3,2]
N = 5
L2 = []
for i in range(N):
    if i in L :
        L2.append(1)
    else :
        L2.append(0)

str(L2)
print(L2)