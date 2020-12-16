#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 17:21:54 2018

@author: jonathancindanomwamba
"""
n = int(input("Factoriel : "))
def Factoriel(N):
    if N > 1:
        return N * Factoriel(N - 1)
    else:
        return 1

for i in range(n+1):
    print(i,"! est ",Factoriel(i))