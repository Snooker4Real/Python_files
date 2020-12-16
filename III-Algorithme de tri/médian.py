#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:15:03 2019

@author: jonathancindanomwamba
"""

def median(L): #L est une liste triée
    N = len(L)
    if N%2==1: #si L à une taille impaire
        return [N//2]
    else :
        return L[N//2-1], L[N//2]

