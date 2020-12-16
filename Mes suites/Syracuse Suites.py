#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:02:13 2018

@author: jonathancindanomwamba
"""

#Suite de Syracuse


x = float(input('X :'))
n = int(input('n fois :'))

def Syracuse(x):
    for i in range(1,n):
        if x%2 == 0:
            x = x/2
        else :
            x = x*3 + 1
    i =i+1
    return x
print(n,':',Syracuse(x))