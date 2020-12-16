#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 19:43:40 2018

@author: jonathancindanomwamba
"""

print("Choisis un nombre entre 0 et 100 dans ta tête et l'ordinateur va le deviner")
input("Taper sur une touche pour commencer")

bornes = [0, 100]
milieu = int(bornes[0] + bornes[1])/2

while bornes[1] - bornes[0]:
    milieu = int(bornes[0]+bornes[1])/2

    reponse = input("Est-ce-que ton nombre est supérieur à " + str(milieu) + "? (o/n)" )
    if reponse == "o":
        bornes = [milieu, bornes[1]]
    elif reponse == "n":
        bornes = [bornes[0], milieu]

reponse = input("Est-ce que ton nom est " + str(bornes[0]) + " ? (o/n) "):
    if réponse == "o":
        print("Ton nombre est " + str(bornes[0]))
    else:
        print("Ton nombre est " + str(bornes[1]))

print(bornes)