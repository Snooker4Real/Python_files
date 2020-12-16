#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 12:47:56 2017

@author: jonathancindanomwamba
"""

#Cette algorithme permet de rechercher par dichotomie

def f(x):
    return x**2 - 2

#On défini la fonction a étudier

def RD(g,a,b,epsilon=10**(-10)) :
    if g(a) == 0:
#Il faudrait le remplacer par abs(f(a))<éta
#Toute valeur inférieure à éta sera considérée comme nulle
        return a
    while b-a > epsilon :
        m = (a+b)/2
        if g(a)*g(m)<=0 :
            b = m
        else:
            a = m
    return (a+b)/2
        
print(RD(f,1,2))