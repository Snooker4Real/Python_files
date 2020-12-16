# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:51:41 2017

@author: admin
"""

def F(M,i,j) :
    M[i], M[j] = M[j], M[i]

def F2(M,i,j) :
    N = len(M) # nombre de lignes
    for k in range(N) : # k est le numéro de ligne
        M[k][i], M[k][j] = M[k][j], M[k][i]

def G(M,i) :
    N = len(M)
    MEVA = 0 # ou M[i][i]
    for k in range(i,N) :
        if abs(MEVA) < abs(M[k][i]):
            MEVA = M[k][i]
    return MEVA

M = [[1,  9, 17,  16,  2,  1],
     [7,  2,  0,   2,  3,  2],
     [0,  7, -9,   5,  7,  3],
     [5,  2,  2,   7, -5,  5],
     [18,-1,  1,  12,  6,  2],
     [-9, 8,  6, -15,  2, -6]]
print(G(M,2))





