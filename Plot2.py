import math
import matplotlib.pyplot as plt
import numpy as np

#read from a file and plot
X,Y =[],[]
with open( '3n+1.txt','r') as f:
    for line in f:
            x = line.split()
            X.append(x[0])
            Y.append(x[1])

plt.plot(X,Y)
plt.show()