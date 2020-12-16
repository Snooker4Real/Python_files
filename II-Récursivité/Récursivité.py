#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:02:52 2018

@author: jonathancindanomwamba
"""

n = int(input('rang() :'))
def U(n):
    r = 2.
    for i in range(n):
        r =0.5*(r+3./r)
    return r
print("r=",U(n))

def u(n):
    if n == 0:
        return 2.
    else:
        return 0.5*(u(n-1)+3/u(n-1))