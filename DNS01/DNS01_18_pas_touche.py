# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:13:07 2017

@author: Thomas
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def ExtractData(Nom) : # Renvoie un tableau H*L*3
    im = Image.open(Nom)     # Lecture de l’image
    L, H = im.size                       # Taille de l’image
    data = im.getdata()           # On récupère les données dans la variable data
    d = np.array(data)             # conversion de data en tableau 
    if len(d[0]) == 3 :
        d = (d[:,0]+d[:,1]+d[:,2])/3
    IMA = d.reshape((H,L))  # On transforme un tableau 1D en tableau avec 2 indices.
    return IMA

# Cette fonction crée une image qui s’appelle « nom » (n’oubliez pas l’extension « .jpg », « .png », …
def CreerImage(IMA,nom) : # IMA est un tableau de dimensions H*L*3. 
     H, L = len(IMA), len(IMA[0]) 
     im = Image.new('RGB',(L,H))
     pix = im.load()
     for i in range(L) :
         for j in range(H) :
             pix[i,j] = tuple(IMA[j,i])    # On rentre pixel par pixel les valeurs de l’image à partir de IMA
     im.save(nom)

def Gray2nb(Ima,Lnb) :
    H, L = len(Ima), len(Ima[0])
    q = 0
    while q*Lnb < L : q = q + 1
    Ima_nb = np.zeros((H,L))
    Min, Max = 0, 0
    for i in range(0,H,q) :
        for j in range(0,L,q) :
            C, S = 0, 0
            for a in range(q) :
                for b in range(q) :
                    if i+a<H and j+b<L :
                        C = C + 1
                        S = S + Ima[i+a,j+b]
            value = int(S/C)
            if value < Min : Min = value
            if value > Max : Max = value
            for a in range(q) :
                for b in range(q) :
                    if i+a<H and j+b<L :
                        Ima_nb[i+a,j+b] = value
    for i in range(0,H) :
        for j in range(0,L) :
            if Ima_nb[i,j]>(Max-Min)/2.+Min :
                Ima_nb[i,j] = 1
            else :
                Ima_nb[i,j] = 0
    return Ima_nb

def Conversion(n,P) :
    r = []
    for i in range(P) :
        r = [n%2] + r
        n = n//2
    if n != 0 : print("Warning!")
    return r

def ImageFromDataEleve(VotreIma,votreL,NOM) :
    IMA = ExtractData(NOM)
    H, L = len(IMA), len(IMA[0])
    q = 0
    while q*votreL < L : q = q + 1
    Ima = []
    for x in VotreIma :
        Ima.append(Conversion(x,votreL))
    VotreIma_nb = np.zeros((H,L))
    for i in range(0,H,q) :
        for j in range(0,L,q) :
            for a in range(q) :
                for b in range(q) :
                    if i+a<H and j+b<L :
                        if (i+a)//q < len(Ima) :
                            VotreIma_nb[i+a,j+b] = 1-Ima[i//q][j//q]
                        else :
                            VotreIma_nb[i+a,j+b] = 0
    return VotreIma_nb

def Note(VotreIma,votreL,NOM) :
    IMA = ExtractData(NOM)
    IMA_nb = Gray2nb(IMA,votreL)
    VotreIma_nb = ImageFromDataEleve(VotreIma,votreL,NOM)
    H, L = len(IMA), len(IMA[0])
    q = L//votreL
    p = q*len(VotreIma)
    if p > H : p=H
    Diff = IMA_nb-VotreIma_nb
    Diff = Diff[:p,:]
    note = 20.*(1-np.sum(Diff**2)/len(Diff)/len(Diff[0]))
    note = note - (len(VotreIma) < 20)*(20-len(VotreIma))
    print(50*'*')
    print("note = ", note,"/20")
    print(50*'*')
    fig = plt.figure()
    plt.subplot(311)
    plt.title("Image différence (fausses couleurs)")
    plt.imshow(Diff)
    plt.subplot(312)
    plt.title("Votre Image")
    plt.imshow(VotreIma_nb)
    plt.subplot(313)
    plt.title("Image calculée par l'ordinateur")
    plt.imshow(IMA_nb)
    plt.show()
    
