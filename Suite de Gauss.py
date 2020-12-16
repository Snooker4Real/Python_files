#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 23:02:05 2018

@author: jonathancindanomwamba
"""

#Suite de Gauss

n = int(input("n :"))

for k in range(1,n):
    S = (n*(n+1))/2
    k = k+1
print("Somme n premiers termes :",S)