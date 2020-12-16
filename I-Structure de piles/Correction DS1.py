#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:04:39 2018

@author: jonathancindanomwamba
"""

def entree_distrib(bonbon, distributeur):
    N = distributeur[0]
    if N ==len(distributeur-1): #N a atteitla capacité
        return "distributeur rempli"
    else:
        distributeur[0]=N+1
        distributeur[N+1]=bonbon
        return distributeur

def est_vide(distributeur):
    return distributeur[0]==0

def nombre(distributeur):
    return distributeur[0]

def sortie_distrib(distributeur):
    N = distributeur[0]
    assert N!=0, "distributeur vide"


def parentheses(exp):
    return []

def empilage(pile,x):
    pile.append(x)

def depilage(pile):
    assert len(pile)!=0, "pile vide"
    return pile.pop()

def parentheses(exp):
    indices_ouvrantes = creer_pile()
    for i in range(len(exp))