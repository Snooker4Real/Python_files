#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:46:17 2018

@author: jonathancindanomwamba
"""

#On charge l'indice de mot dans phrase
def MotDansPhrase(mot,phrase):
    N = len(phrase)
    P = len(mot)
    L = [] # liste vide
    for i in range (N):
        if phrase[i:i+P] == mot:
            L.append(i)
        return L
mot = "Paris"
phrase = "Londres Paris Paris Moscou Pris"
a = MotDansPhrase(mot,phrase)
print(a)