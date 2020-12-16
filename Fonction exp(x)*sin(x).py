#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:03:57 2017

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(x)*np.sin(x)

x = np.linspace(-1,2,2000)
plt.plot(x,f(x))