import numpy as np
import scipy as sp
from scipy.integrate import odeint
import scipy.misc as spm

def x_integ(y0,x):
    return sp.sin(x)**2

def x_diff(x):
    return sp.sin(x)**2

y0 = 0
x = np.linspace(0,10,101)

sol = odeint(x_integ,y0,x)
sol2 = spm.derivative(x_diff,x,dx=1e-6)

import matplotlib.pyplot as plt

plt.plot(x,sol)
plt.plot(x,sol2)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Integrated','Diffrentiated'])
plt.show()