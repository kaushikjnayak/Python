import numpy as np
import math

a1 = np.round(np.random.randn(5 )* math.pow(10,5))
print (a1)
#svarious operations of 1 d array
print (a1.sum())
print (a1.mean())
print (a1.max())

#returns array with intermediate  sum .
print (a1.cumsum())


#index of maximum element
print (a1.argmax())

#sum of all positive elements
print (a1[a1 > 0].sum())

#count of Positive elements
print ( (a1 > 0).sum())


a1.sort()
print (a1)

a2 = np.round(np.random.randn(4,4 )* math.pow(10,5))
print (a2)
a3 = a2

print ('#############')
#sort along x axis
a2.sort(1)

print (a2)
print ('#############')

#sort the whole matrix
a4 = a3.sort()
print (a4)

