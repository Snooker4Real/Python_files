#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 16:40:36 2018

@author: jonathancindanomwamba
"""

import numpy as np
import matplotlib.pyplot as plt
import PIL as Image

def ExtractData(Nom) : # Renvoie un tableau H*L*3
    im = Image.open(Nom)     # Lecture de l’image
    L, H = im.size # Taille de l’image
    data = im.getdata() # On récupère les données dans la variable data
    d = np.array(data) # conversion de data en tableau
    IMA = d.reshape((H,L,3)) # On transforme un tableau 1D en tableau avec 3 indices.
    return IMA # Renvoie un tableau de dimension H*L*3

# Cette fonction crée une image qui s’appelle « nom » (n’oubliez pas l’extension « .jpg », « .png », ...
def CreerImage(IMA,nom) : # IMA est un tableau de dimensions H*L*3. 
    H, L = len(IMA), len(IMA[0])
    im = Image.new('RGB',(L,H))
    pix = im.load()
    for i in range(L) :
        for j in range(H) :
            pix[i,j] = tuple(IMA[j,i])
    im.save(nom)
ima = ExtractData("mouvement_02_92.jpg")
fig = plt.figure()
plt.imshow(ima[:,:,2])
plt.show()
ima[:,:,1] = 0*ima[:,:,1] # On met le zéro sur le vert
ima[:,:,2] = 0*ima[:,:,2] # On met le zéro sur le bleu
CreerImage(ima,"ImageRouge.png")

for i in range(L) :
    for j in  range(H):
        pix[i,j] = tuple(IMA[j,i])
    im.save(nom)
    def TrouvePL(ima):
        H, L = len(ima), len(ima[0])
        for i in range(L):
            for i in range(H):
                R = ima[j,i,0]  #Niveau de rouge colonne i ligne j
                V = ima[j,i,1]
                B = ima[j,i,2]
                if R > seuil and V > seuil and B > seuil :
                    X.append(i)
                    Y.append(j)
    if len(X) == 0:
        return 0, 0
    xG = sum(X)/len(X)
    yG = sum(Y)/len(Y)
    return xG, yG

def Croix(x0,y0,ima) :
    X0 = int[x0]
    Y0 = int[y0]
    for i in range(50):
        pass
    for j in range(50):
        pass

ima = ExtractData("mouvement_02_92.jpg")
print(TrouvePL(ima))
fig = plt.figure()
plt.imshow(ima[:,:,2])
plt.show()