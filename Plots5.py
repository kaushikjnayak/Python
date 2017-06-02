import numpy as np
import matplotlib.pyplot as plt

#a 1000 x 2 array from data.
data = np.random.rand(1000, 2)


#scatter all the points 
plt.scatter(data[:,0] ,data[:,1] )

plt.show()