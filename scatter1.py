import matplotlib.pyplot as plt
import numpy as np


nrange = np.random.standard_normal(1000)
arange = np.arange(len(nrange))
print ( nrange )

#blank centre
plt.scatter(nrange,arange,color='1.0',edgecolors='0.0')
plt.show()
#triangular marking

plt.scatter(nrange,arange,marker='^')

plt.show()