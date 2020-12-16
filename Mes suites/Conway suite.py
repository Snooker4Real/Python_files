#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:33:09 2018

@author: jonathancindanomwamba
"""

# conway.py

z = int(input('Terme de rang (<30 de préférence) : '))

def Next(terme):
    resultat = ''
    dernier = terme[0]
    n = 1
    for C in terme[1:]:
        if C == dernier:
            n = n+1
        else:
            resultat = resultat + str(n) + dernier
            dernier = C
            n = 1
    return resultat + str(n) + dernier
 
terme = '1'
for i in range(z+1):
    print("u (",i,") :",terme)
    terme = Next(terme)