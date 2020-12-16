#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:48:25 2017

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 4*x**2-7*x+3

x = np.linspace(-5,5,2000)

plt.plot(x,f(x))
plt.show()
