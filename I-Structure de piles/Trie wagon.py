#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:57:23 2018

@author: jonathancindanomwamba
"""

def creer_pile():
    return []

def empiler(pile,x):
    return pile.append(x)

def depiler(pile):
    assert len(pile)!=0, "pile vide"
    return pile.pop()

def sommet(pile):
    return pile[-1]

def est_vide(pile):
    return len(pile)==0

def renverserpile():
    inverse = creer_pile()
    while not(est_vide(pile)):
        empiler(inverse,depiler(pile))
    for i in range(len(inverse)):
        empiler(pile,inverse[-1-i])

def copierpile(pile):
    copie = creer_pile()
    for i in pile:
        empiler(copie,i)
    return copie

def dernierpremier(pile):
    s = sommet(pile)
    for i in range(len(pile)-1):
        pile[-i-1]=pile[-i-2]
        pile[0]=5
    return pile

v1 = creer_pile()
v2 = creer_pile()

def repartir(v0,v1,v2):
    empiler(v1,depiler(v0))
    while not(est_vide(v0)):
        if sommet(v0)<sommet(v1):
            empiler(v1, depiler)
        elif est_vide(v2) or sommet(v0)<sommet(v2):
            empiler(v2,depiler(v0))
        else:
            return v0,v1,v2

def reunir(v0,v1,v2):
    while not (est_vide(v1)) and not (est_vide(v2)):
        if sommet(v1)<sommet(v2):
            empiler(v0, depiler(v1))
        else:
            empiler(v0, depiler(v2))
    if est_vide(v2):
        while not(est_vide(v2)):
            empiler(v0,depiler(v2))
    elif est_vide(v2):
        while not(est_vide(v1)):
            empiler(v0,depiler(v1))

def tri(v0):
    repartir(v0,v1,v2)
    while not(est_vide(v0)):
        reunir(v0,v1,v2)
        repartir(v0,v1,v2)
    reunir(v0,v1,v2)
    return v0