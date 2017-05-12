import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([4,6,7,8,80])

aidx = [2,3,4]

# Print elements at index 2,3,4  of a
print (a[aidx])

a = np.arange(20)
a1 = a.reshape(5,4)
a2 = a.reshape(2,5,2,1)

print (a1)
print (a2)


#Transpose the array to its original form.

print( a.T)

#Transpose the array with axis provided.
print (a2.transpose((1,2,3,0)))

