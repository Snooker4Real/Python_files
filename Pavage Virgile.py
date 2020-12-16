import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y=np.exp(x)*np.sin(x)
    return y
    
x=np.linspace(-1.,2.,100)
y=f(x)

plt.plot(x,y)
#plt.show()

def liste(L,N):
    L2=[]
    for i in range(N):
        if i in L:
            L2.append(1)
        else:
            L2.append(0)
    return L2


def string(L,N):
    a=''
    for i in range(N):
        if i in L:
            a=a+'1'
        else:
            a=a+'0'
    return a
    
L=[3,2]
N=5
#print(liste(L,N))
#print(string(L,N))





def coordonnées1(P):
    x=[]
    y=[]
    for i in range(P-1):
        x.append((i+1)/P)
        y.append(0.)
    return x,y

def coordonnées2(P):
    x=[]
    y=[]
    for i in range(P-1):
        x.append(1.)
        y.append((i+1)/P)
    return x,y

def Rotation(x,y):
    x2=x[:]
    y2=y[:]
    for i in range(len(x)):
        x2[i],y2[i]=-y[i],x[i]
    return x2,y2

def Translation(x,y,Dx,Dy):
    x2=x[:]
    y2=y[:]
    for i in range(len(x)):
        x2[i],y2[i]=x[i]+Dx,y[i]+Dy
    return x2,y2


def GenereUnCarreau():
    global xB1,yB1,xB2,yB2
    xB4,yB4 = Rotation(xB1,yB1)
    xB4.reverse()
    yB4.reverse()
    xB3,yB3=Translation(xB2,yB2,-1,0)
    xB3,yB3=Rotation(xB3,yB3)
    xB3,yB3=Rotation(xB3,yB3)
    xB3,yB3=Rotation(xB3,yB3)
    xB3,yB3=Translation(xB3,yB3,0,1)
    xB3.reverse()
    yB3.reverse()
    xFinal=[0.]+xB1+[1.]+xB2+[1.]+xB3+[0.]+xB4+[0.]
    yFinal=[0.]+yB1+[0.]+yB2+[1.]+yB3+[1.]+yB4+[0.]
    return xFinal,yFinal



P=4
xB1,yB1=coordonnées1(P)
xB2,yB2=coordonnées2(P)
xB=xB1+xB2
yB=yB1+yB2

xF,yF=GenereUnCarreau()


fig=plt.figure()
plt.plot(xF,yF,"r-")
plt.plot(xF,yF,"r*")
plt.plot(xF,yF,"r-")
plt.plot(xF,yF,"r*")
plt.axis([-0.1,1.1,-0.1,1.1])
plt.show()










































