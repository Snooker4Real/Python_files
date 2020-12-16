#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:47:49 2018

@author: jonathancindanomwamba
"""

def deplacement_elementaire(tours,i,j):
    k=0
    while tours[i][k]!=0:
        k=k+1
#Quand la boucle while est terminée, le sommet de tours[i] est tours[i][]
#[6,5,4,3,0,0,0,0]

def jeu7(tours):
    jeu6(tours,0,1)
    deplacement_elemetaire(tours,0,2)
    jeu6(tours,1,2)

def jeu6(tours,i,j):
    k = 3-i-j #car les indices des colonnes sont 0, 1 ou 2
#k esr l'indice de la tour qui n'est ni i ni j
    jeu5(tours,i,j)
    deplacement_elementaire(tours,i,j)
    jeu5(tours,k,j)

def jeu5(tours,i,j):
    k = 3-i-j
    jeu4(tours,i,k)
    deplacement_elemenatire(tours,i,j)
    jeu4(tours,k,j)

def jeu4(tours,i,j):
    k = 3-i-k
    jeu3(tours,i,j)
    deplacement_elementaire(tours,i,j)
    jeu3(tours,k,j)

def jeu3(tours,i,j):
    k = 3-i-j
    jeu2(tours,i,k)
    deplacement_elemantaire(tours,i,j)
    jeu2(tours,k,j)

def jeu2(tours,i,j):
    k = 3-i-j
    deplacement_elementaire(tours,i,k)
    deplacement_elementaire(tours,i,j)
    deplacement_elemantaire(tours,k,j)

def jeu(n,tours,i,j):
    k = 3-i-j
    if n==2:
        deplacement_elementaire(tours,i,k)
        deplacement_elementaire(tours,i,j)
        deplacement_elementaire(tours,k,j)
    else:
        jeu(n-1,tours,i,k)
        deplacement_elementaire(tours,i,j)
        jeu(n-1,tours,k,j)

def jouer(n,tours):
    jeu(n-1,tours,0,1)
    deplacement_elementaire(tours,0,2)
    jeu(n-1,tours,1,2)
    return tours

