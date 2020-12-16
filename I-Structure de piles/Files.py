#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 14:35:03 2018

@author: jonathancindanomwamba
"""

def creerfile(c):
    File=(c+1)[None]
    File[0]=0
    return File

def entre_file(File,client):
    c = len(File)-1
    N=File[0]
    if N>=c:
        return "plus de place, désolé"
    elif client[1]<18:
        return "interdit! retourne chez ta mère"
    else:
        for i in range(N):
            File[N-i+1]=File[N-i]
        File[1]=client
        File[0]=N+1
    return File

def sortie_file(File):
    N = File[0]
    assert N!=0,"file vide"
    client=File[N]
    File[N]=None
    N =N-1
    return client

