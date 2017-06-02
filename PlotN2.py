import matplotlib.pyplot as plt
import numpy as np


X = np.arange(1,91)

Y = np.sin(X*np.pi/180)

Y2 = np.cos(X*np.pi/180)

plt.plot(X,Y,'g', label = 'SIN(x)', linewidth = 3.)
plt.plot(X,Y2,'r--', label = 'COS(x)', linewidth = 2.)

#grid colour = blue, style is dot & dash
plt.grid(linewidth = '2' , c='b' , linestyle = '-.')

plt.legend(loc='center', title = 'Type of curve', fancybox =True)
plt.show()