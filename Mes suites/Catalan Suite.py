#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:31:02 2018

@author: jonathancindanomwamba
"""

#Suite de Catalan

n = int(input('rang() :'))
def catalan(n):
    c = (n+1)*[1]
    for i in range(1,n+1):
        c[i] = sum([c[k]*c[i-1-k] for k in range(0,i)])
    return(c[n])
print(catalan(n))