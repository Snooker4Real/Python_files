import numpy as np
import matplotlib.pyplot as plt

def F(x,t) :
	return x
N = 1000
t0, t1 = 0., 5.
t = np.linspace(t0,t1,N)
x = 1.	#C.I
Lx = np.zeros(N)    #Pour conserver tout ce qui est calculé
Lx[0] = x
for n in range(1,N):
	h = t[n]-t[n-1]
#   	x = x +F(x,t)*h
"""RK4"""
    K1 = F(x, t[n-1])
    K2 = F(x+K1*h/2,t[n]+h/2)
    K3 = F(x+K2*h/2,t[n]+h/2)
    K4 = F(x+K3*h,t[n]+h)
    x = x + (K1+2*K2+2*K3+K4)/6*h
"""******"""

	Lx[n] = x
fig = plt.figure()
plt.plot(t,Lx)
plt.show()
