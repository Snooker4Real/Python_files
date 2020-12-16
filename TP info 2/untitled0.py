#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 13:40:30 2018

@author: jonathancindanomwamba
"""

def puissance(x,n):
    if n==0:
        return 1
    else :
        return x*puissance(x,n-1)

#def puissance