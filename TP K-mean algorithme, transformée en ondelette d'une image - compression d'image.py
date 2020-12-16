#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:59:42 2018

@author: jonathancindanomwamba
"""

import random as r
import numpy as np
import matplotlib.pyplot as plt

def InitPoints():
    N = 30
    sigma = 1
    xA, yA = 10, 5
    xB, yB = 3, 1
    X, Y = [], []   #On initialise deux listes vides
    for i in range(N):
        if r.random() < 0.5 :   #On choisit au hasard si on met un point
            # a proximité du point A ou du point B.
            x = r.gauss(xA,sigma)
            y = r.gauss(yB,sigma)
        else:
            x = r.gauss(xB,sigma)
            y = r.gauss(yB,sigma)
        X.append(x)
        Y.append(y)
    return X, Y