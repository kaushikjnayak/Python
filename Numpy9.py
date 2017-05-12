import numpy as np

a = np.random.rand(5)

print (a)

#Save the contents of array into a local file.
np.save("C:/Users/kaushik/Desktop/Test_numpy",a)


#Load the contents back to array b
b = np.load("C:/Users/kaushik/Desktop/Test_numpy.npy")

print (b)

import random
for i in range(20):
   print ( random.randint(0, 5))