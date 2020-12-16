#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 15:47:50 2018

@author: jonathancindanomwamba
"""

from turtle import *
import matplotlib.pyplot as plt

b = "bleu"
o = "orange"

def carre(cote):
    fillcolor(o)
    down()
    begin_fill()
    for i in range(4):
        forward(cote)
        left(90)
    up()
    end_fill()

def triangle(cote):
    down()
    begin_fill()
    for i in range(3):
        forward(cote)
        right(120)
    end_fill()

c = complex(-0.8,-0.1)
def mandelbrot(n):
    l = [0]
    for i in range (n):
        l.append(l[-1]**2+c)
    return l
