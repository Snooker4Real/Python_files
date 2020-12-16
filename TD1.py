#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:49:02 2018

@author: jonathancindanomwamba
"""

#from random import randrange

#L=[2,9,6,5,3,1,8]

"""1"""

"""
i=1
j=2
def echange(L,i,j):
    L[i],L[j]=L[j],L[i]
    return(L)
print("L=",echange(L,i,j))"""


"""2"""

"""
def croissant(L):
    i=L[0]
    for j in L:
        if j<i:
            return False
        i=j
    return True
print(croissant(L))
"""

#    for i in range(len(L)-1):
#        if not L[i]<=L[i+1]:
#            return False
#        return True
#    i=L[0]
#    for j in L:
#        if i>j:
#            return False
#        i=j
#        return True
#print(croissant(L))

"""3"""

"""
def doublon(L):
    return list(set(L))
print("L=",doublon(L))
"""

"""4"""

"""
def minmax(L):
    a = min(L)
    b = max(L)
    return a,b
print("(min,max)=",minmax(L))
"""

"""6"""
"""
def est_trié(L):
    if len(L) == 0:
        return True
    dL = [ L[i+1] - L[i] for i in range(len(L)-1) ]
    for e in dL:
        if e < 0 :
            return False
    return True

def changer(L):
    for i in range(len(L) - 1, 0, -1):
        j = range(i + 1)
        echange(L,i,j)
    return L

def trier(L):
    while est_trié(L) == False:
        L = changer(L)
        print(L)
    return L
print("L=",trier(L))
"""


"""
def trier(L):
    return sorted(L)
print("L=",L)
print("L_trié=",trier(L))
"""

"""7"""
#n = int(input("n="))
L=[]
def factpremiers(n):
    if n>1:
        for i in range(2,n):
            while n%i==0:
                print(i)
                n=n//i
    return

