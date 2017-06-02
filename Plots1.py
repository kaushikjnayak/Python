import math
import matplotlib.pyplot as plt
import numpy as np


#plot sine and cosine

X = np.linspace(0,2*np.pi,100)

Ysin = np.sin(X)
Ycos = np.cos(X)

#plot in red and green
plt.plot(X,Ysin,'r')
plt.plot(X,Ycos,'g')

plt.show()