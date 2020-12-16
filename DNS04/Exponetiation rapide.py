#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 00:26:09 2018

@author: jonathancindanomwamba
"""

#Exponentiation rapide

x = float(input("x= "))
n = int(input("n= "))

#def f(x):
#    y = x
#    for i in range(1,n):
#        y = y * x
#    return y
##y = f(x)
#print("x^n= ",f(x))

#def g(x,n):
#    if n == 1:
#        return x
#    else:
#        if n%2 == 0:
#            z = g(x,n/2)
#            return z*z
#        else:
#            z = g(x,(n-1)/2)
#            return z*z*x
#print("x^n = ",g(x,n))
#
#def Bin(n):
#    s = ' '
#    while n != 0:
#        if n % 2 == 1:
#            s = '1' + s
#        else :
#            s = '0' + s
#        n = n//2
#    return s
#print("bin(n) = ",Bin(n))

def fact(n):
    rn = int(n**0.5)        #rn = sqrt(n)
    p = 1
    for i in range(1, rn+1):
        if n%i ==0:
            p = int(i)
            q = n//p
    return p, q
p, q = fact(n)
print("p, q = ", fact(n))

def h(x,n):
    if n == 1:              #Cas de base
        return x
    else:
        if p == 1:          # n premier
            z = h(x,n-1)
            return z*z
        else :              # n non-premier
            y = h(x,p)
            z = h(y,q)
            return z
    return z
#z = h(x,n)
print("z = ",h(x,n))