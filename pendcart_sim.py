import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# params
M = 2
m = 1
l = 0.5
g=9.8
print('l is:', l)

def dX_dt(X,t):
    dX0 = X[2]
    dX1 = X[3]
    dX2_num = m*g*np.cos(X[1])*np.sin(X[1]) - m*l* X[3]**2 * np.sin(X[1])
    dX2_den = (M + m*np.sin(X[1])**2)/l
    dX2 = dX2_num/dX2_den
    dX3 = (dX2*np.cos(X[1]) + g*np.sin(X[1]))/l
    dX = [dX0, dX1, dX2, dX3]
    return dX

t = np.linspace(0,10,500)

sol = odeint(dX_dt, [0.1, 0.1, 0.1, 0.1],t)
print(np.shape(sol[:,1]))
print(np.shape(t))
#plt.plot(t, sol[:,0], t, sol[:,1], t, sol[:,2], t, sol[:,3])
plt.plot(t, sol[:,0])
plt.show()
