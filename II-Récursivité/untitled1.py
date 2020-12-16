#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:52:14 2018

@author: jonathancindanomwamba
"""

def u(n):
    if n ==0:
        return 2
    else:
        x = u(n-1)
        return 0.5*((x+3))/x