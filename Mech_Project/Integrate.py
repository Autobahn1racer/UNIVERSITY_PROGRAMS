import numpy as np
import scipy as sp
from scipy.integrate import odeint

def dy_dx(y,x):
    return x+y

y0 = 0
x = np.linspace(0,10,101)

sol = odeint(dy_dx,y0,x)

import matplotlib.pyplot as plt

plt.plot(x,sol)
plt.xlabel('x')
plt.ylabel('y')
plt.show()