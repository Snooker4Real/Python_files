#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 22:22:48 2018

@author: jonathancindanomwamba
"""

def fib(n):
    n =10
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()