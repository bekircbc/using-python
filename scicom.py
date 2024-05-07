import numpy as np
from scipy.integrate import odeint

def model(y, t):
  dydt = -0.1 + y
  return dydt

y0 = 1.0

t = np.linspace(0,20,100)

sol = odeint(model, y0, t)

import matplotlib.pyplot as plt

plt.plot(t, sol)
plt.xlabel('Time')
plt.ylabel('Solution')
plt.show()
