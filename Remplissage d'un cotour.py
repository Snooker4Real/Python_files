#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 13:51:56 2017

@author: jonathancindanomwamba
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def F1(x,y):
    norme = np.sqrt(x**2+y**2)
    tx, ty = x/norme, y/norme
    nx, ny = -y/norme, x/norme
    return nx, ny, tx, ty

def F2(xA, yA, xB, yB, x, y):
    nx, ny, tx, ty = F1(xB-xA,yB-yA)
    # coordonnée de AM selon le vecteur n
    AMn = nx*(x-xA) + ny(y-yA)
    # coordonnée de AM selon le vecter t
    AMt = tx*(x-xA) + ty*(y-yA)
    return AMn, AMt

def F3(xA, yA, xB, yB, x, y):
    AMn, AMt = F2(xA, yA, xB, yB, x, y)
    AB = np.sqrt((xB-xA)**2+(yB-yA)**2)
    if 0 < AMn < AB :
        return abs(AMt)
    elif AMn<=0:
        return np.sqrt(AMn**2+AMt**2)
    else:
        return np.sqrt((x-xB)**2+(y-yB)**2)

def F4(Lx, Ly, x, y, L, H, epsilon = 2):
    if x < epsilon :
        return True
    
    N = len(Lx)
    for i in range(N-1):
        xA, yA = Lx[i], Ly[i]
        xB, yB = Lx[i+1], Ly[i+1]
        d = F3(xA, yA, xB, yB, x, y)
        if d< epsilon:
            return True


def F5(H,L,i0,y0):
    INFO = np.zeros((H,L), dtype='int')
    H,L = len(INFO),len(INFO[0])
    INFO[j0,i0] = 1
    while True :
        if F5bis(INFO, Lx, Ly):
            return INFO
""" La fonction F5bis() test dans INFO tous les voisins des pixels qui sont à 1
(celle sont les voisins n'ont pas encore été traités) """

def F5bis(INFO,Lx,Ly):
    H, L = len(INFO), len(INFO[0])
    for j in range(H):
        for i in range(L):
            """On parcourt l'image de gauche à droite et de haut en bas."""
            if INFO[j,i] ==1 :
                """Comme on teste tous les voisins INFO[i,j] passe à 2"""
                INFO[j,i] = 2
                for (a,b) in [(-1,0),(-1,1),(-1,-1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]:
                    if INFO[j+b,i+a]== 0 and not F4(Lx,Ly,i+a,j+b,L,H):
                        """On vérifie que les pixel pixel voisin est à zéro et
                        que le pixel est loin du contour donc dans le contour"""
                        INFO[j+b,i+a] = 1
    """Ayant de sortir de la fonction, on renvoie False
    il n'y a plus aucun 1 dans INFO"""
    test = np.sum(INFO == 1)
    if test == 0:
        return False
    return True


NOM1 = "IMG_0706.jpg"
Lx = [50,300,400,500,50,50]
Ly = [50,50,300,300,50]
H, L = len(INFO), len(INFO[0])
i0, j0 = 75, 75
INFO = F5(H,L,i0,j0,Lx,Ly)
for i in range(L):
    for j in range(H):
        if INFO[j,i] == 2:
            INFO[j,i,0] = 255 - IMA[j,i,0]
            INFO[j,i,1] = 255 - IMA[j,i,1]
            INFO[j,i,2] = 255 - IMA[j,i,2]
CreerImage (INFO,"justeLeContour.jpg")

"""def ExtractData(Nom) : # Renvoie un tableau H*L*3
im = Image.open(Nom) L, H = im.size # Lecture de l’image
data = im.getdata() # Taille de l’image
d = np.array(data) # On récupère les données dans la variable data # conversion de data en tableau

IMA = d.reshape((H,L,3)) # On transforme un tableau 1D en tableau avec 3 indices.
return IMA

# Cette fonction crée une image qui s’appelle « nom » (n’oubliez pas l’extension « .jpg », « .png », ...
def CreerImage(IMA,nom) : # IMA est un tableau de dimensions H*L*3.
H, L = len(IMA), len(IMA[0]) im = Image.new('RGB',(L,H)) pix = im.load()
for i in range(L) :
for j in range(H) :
pix[i,j] = tuple(IMA[j,i]) # On rentre pixel par pixel les valeurs de l’image à partir de IMA
im.save(nom)

NOM1 = "image1.jpg"
IMA1 = ExtractData(NOM1) # On lit une image

# Définition du contour
x = np.array([112,118,131,163,209,239,278,321,366,395,419,433, 446,454,455,438,432,403,348,261,199,149,122,112])
y = np.array([369,436,528,573,600,614,623,610,579,556,506,454, 409,394,366,361,337,303,281,276,277,299,325,369])

# Création d’une image
IMA3 = np.zeros((H, L, 3), dtype = 'int') # image noire pour l’instant (qu’il faut modifier)
                                            # image avec L colonnes et H lignes
# Une fois l’image IMA3 complétée on peut créer un fichier .jpg ou .png.
CreerImage(IMA3,"VotreImage.jpg")"""