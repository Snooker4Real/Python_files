# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:23:26 2017

@author: thoma
"""
import numpy as np
import matplotlib.pyplot as plt
import random as r

def GenerationUnCarreau(x,y) :
    global P
    x0, y0 = Rotation(x[:P-1],y[:P-1])
    x1, y1 = Translation(x[P-1:],y[P-1:],-1,0)
    x2, y2 = Rotation(x1,y1)
    x2, y2 = Rotation(x2,y2)
    x2, y2 = Rotation(x2,y2)
    x3, y3 = Translation(x2,y2,0,1)
    x4, y4 = x[:P-1], y[:P-1]
    x5, y5 = x[P-1:],y[P-1:]
    x0.reverse()
    y0.reverse()
    x3.reverse()
    y3.reverse()
    return [0.]+x4+[1.]+x5+[1.]+x3+[0.]+x0, [0]+y4+[0.]+y5+[1.]+y3+[1.]+y0
    
def Rotation(x,y) :
    X, Y = [], []
    for i, j in zip(x,y) :
        X.append(-j)
        Y.append(i)
    return X,Y

def Translation(x,y,Deltax,Deltay):
    X, Y = [], []
    for i, j in zip(x,y) :
        X.append(i+Deltax)
        Y.append(j+Deltay)
    return X,Y

def GenerationPavage(x,y) :
    x, y = GenerationUnCarreau(x,y)
    for i,j in zip(x,y) :
        print(i,j)
    X, Y = [x], [y]
    for i in range(3) :
        x, y = Rotation(x,y)
        X.append(x)
        Y.append(y)
    N = len(X)
    for i in range(N) :
        x, y = X[i], Y[i]
        X0, Y0 = Translation(x,y,2,0)
        X.append(X0)
        Y.append(Y0)
    N = len(X)
    for i in range(N) :
        x, y = X[i], Y[i]
        X0, Y0 = Translation(x,y,0,2)
        X.append(X0)
        Y.append(Y0)
    return X,Y

def onclick(event):
    global XX, YY, Lx, Ly, INFO, xad, yad, iad, P
    c_x = event.x
    c_y = event.y
    print(20*'_','INFO=',INFO, 20*'_')
    print(f(c_x,c_y))
    XX, YY = f(c_x,c_y)
    if INFO == 0 :
        xad, yad, iad = TrouveLePoint()
        plt.plot(xad,yad,'bo')
        print(xad, yad)
    elif INFO == 1 :
        Lx[iad] = XX
        Ly[iad] = YY
        print(XX, YY)
        AffichePavage()
    INFO = 1-INFO
    
def f(x,y) :
    x0, y0 = 104, 69
    X0, Y0 = -0.987097, -1.00371
    x1, y1 = 549, 397
    X1, Y1 = 2.96048, 2.91739
    X = (x-x0)/(x1-x0)*(X1-X0) + X0
    Y = (y-y0)/(y1-y0)*(Y1-Y0) + Y0
    return X, Y

def TrouveLePoint() :
    global XX, YY, Lx, Ly, INFO, xad, yad, iad, P
    L = []
    print("len(Lx)=",len(Lx))
    for x,y in zip(Lx, Ly) :
        _ = np.sqrt((x-XX)**2+(y-YY)**2)
        L.append(_)
    Min = L[0]
    iMin = 0
    for i, j in enumerate(L) :
        if j < Min : 
            Min, iMin = j, i
    return Lx[iMin], Ly[iMin], iMin

def AffichePavage() :
    global XX, YY, Lx, Ly, INFO, xad, yad, iad, P
    plt.clf()
    plt.draw()
    plt.plot(Lx[:2*P],Ly[:2*P],'*g')
    X, Y = GenerationPavage(Lx,Ly)
    for x,y in zip(X,Y) :
        plt.plot(x,y,'r-')

P = 8
Lx, Ly = [], []
for i in range(1,P) :
    Lx.append(i/P)
    Ly.append(0.)
for i in range(1,P) :
    Lx.append(1.)
    Ly.append(i/P)


N = len(Lx)
XX, YY = 0, 0 # Variable globale
INFO = 0
xad, yad, iad = 0, 0, 0

fig = plt.figure()
plt.plot(Lx[:2*P],Ly[:2*P],'*g')
X, Y = GenerationPavage(Lx,Ly)
for x,y in zip(X,Y) :
    plt.plot(x,y,'r-')
fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

## On modifie le premier segment horizontal
#i = r.randint(0,P-1)
#a = 0.1*(r.random()-0.5)
#b = 0.1*(r.random()-0.5)
#Lx[i] = Lx[i] + a
#Ly[i] = Ly[i] + b
#Lx[-i] = Lx[-i] - b
#Ly[-i] = Ly[-i] + a
## On modifie le second segment vertical
#i = r.randint(P,2*P-1)
#a = 0.05*r.random()
#b = 0.05*r.random()
#Lx[i] = Lx[i] + a
#Ly[i] = Ly[i] + b
#Lx[-i] = Lx[4*P-i] + b
#Ly[-i] = Ly[4*P-i] - a




#axes = plt.gca()
#b = axes.xaxis.get_view_interval()
#print(b)




