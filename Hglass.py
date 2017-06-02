import sys
import numpy as np

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


nparray =np.array(arr)
array1 = []
for i in range(4):
  for j in range(4):
    array1.append(np.sum(nparray[i:3+i,j:3+j]))

print (max(array1))
