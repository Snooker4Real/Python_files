#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:23:25 2018

@author: jonathancindanomwamba
"""

import turtle as tr


def decale_gauche(largeur): #décale vers la gauche de largeur pixels
    tr.left(180)
    tr.penup()
    tr.forward(largeur)
    tr.pendown()
    tr.left(180)
    
def decale_droite(hauteur):
    tr.left(90)
    tr.penup()
    tr.forward(hauteur)
    tr.pendown()
    tr.left(90)
    
def koch(n,longueur):
    tr.speed(0)
    tr.pencolor('blue')
    tr.shape("turtle")
    
    if n == 0:
        tr.forward(longueur)
    else:
        koch(n-1,longueur/3)
        tr.left(60)
        koch(n-1,longueur/3)
        tr.right(120)
        koch(n-1,longueur/3)
        tr.left(60)
decale_gauche(300)
decale_droite(-200)
koch(4,30)