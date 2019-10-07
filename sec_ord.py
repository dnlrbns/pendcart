import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

def dU_dx(U, t):
    return [U[1], -2*U[1] - 2*U[0] + np.cos(2*t)]

U0 = [0, 0]
ts = np.linspace(0, 10, 200)
Us = odeint(dU_dx, U0, ts)
ys = Us[:,0]

plt.plot(ts,ys)
plt.show()
