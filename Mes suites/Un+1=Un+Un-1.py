#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 13:15:10 2018

@author: jonathancindanomwamba
"""

n = int(input('n :'))

def NextStep(s):
    s_next = ''
    for i in s:
        if i == "L":
            s_next = s_next + "Ll"
        if i == "l":
            s_next = s_next +"L"
    return s_next
s = "l"
for i in range(n):
    print(len(s))
    s = NextStep(s)