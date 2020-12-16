#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:51:42 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)
for i in range(1000):
    x = np.linspace(-10,10,i)
    y = f(x)
    plt.plot(x,y)
    