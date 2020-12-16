#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 06:56:47 2018

@author: jonathancindanomwamba
"""

def creer_pile(c):
    pile = (c+1)*[None]
    pile[0]=0 
    return pile

def empiler(pile,x):
    N = pile[0]
    if N>=len(pile)-1:
        return "pile pleine"
    else:
        pile[N+1]=x
        pile[0]=N+1
        return pile

def depiler(pile):
    N = len(pile)
    if N==0:
        return "pile déjà vide"
    else:
        s = pile[N]
        pile[N]=None
        pile[0]=N-1
        return s

def taille(pile):
    return pile[0]

def est_vide(pile):
    if pile[0]==0:
        return True
    else:
        return False

def sommet(pile):
    return pile[pile[0]]

def empiler_bis(pile,x):
    N=pile[0]
    assert N < len(pile)-1, "la pile est déjà pleine"
    pile[N+1]=x
    pile[0]=N+1
    return pile

def creer_pile_c_var():
    return []

def empilage(pile,x):
    pile.append(x)
    return pile

def empilage0(pile,x):
    return pile.append(x)

def depilage(pile):
    assert len(pile)!=0, "pile déjà vide"
    return pile.pop()

