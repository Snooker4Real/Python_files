#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:44:20 2018

@author: jonathancindanomwamba
"""
n = 10
def F(n):
    if n < 2 : return 1
    return F(n-1) + F(n-2)
print(F(n))