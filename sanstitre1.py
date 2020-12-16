#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 15:04:45 2017

@author: jonathancindanomwamba
"""

import numpy as np
R=10
E=10
A = np.array([
        [0., 0., 0., 0., 1., -1., -1.],
        [0., 1., 0., 0., 0, -R,    0.],
        [0., 0., 1., 0., 0., 0.,   -R],
        [0., 0., 0., 1., 0., 0.,   -R],
        [1., 0., 0., 0., -R, 0.,   0.],
        [1., 0., 1., 1., 0., 0.,   0.],
        [0.,-1., 1., 1., 0., 0.,   0.]])

B = np.array([0, 0, 0, 0, 0, E, 0])

X = np.linalg.solve(A,B)

print ("u=",X[3])