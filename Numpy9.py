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

#Divide the range 1,60 into 12 equally spaced divisions.
#endpoint=False makes ending no(60.0 here) to not appear.
adiv = np.linspace( 0.0,60.0,endpoint=False,num=12)

print (adiv)

n3 = np.loadtxt('3n+1.txt')

print (n3)