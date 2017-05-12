import numpy as np

a = np.arange(10)
b = np.arange(10)

#sum of all elements
c = np.sum(a)

# Adding the elements ( not append - like normal lists)
c2 = a + b

#difference between elem and prev elem
d = np.diff(c2)

print (c)

print (c2)

print (d)

#Create a combination of x,y co-ordinate element from meshgrid.Each x and y are 5x5 matrices with
# elements (0..4)x5

x,y = np.meshgrid(np.arange(5),np.arange(5))

print (x)
print (y)

#plot the grids using matplotlib
import matplotlib.pyplot as plt
#plt.plot(x,y, marker='.', color='k', linestyle='none')
#plt.show()

#compute √ (x^2 + y^2) from z and y to yield z

z = np.sqrt(x ** 2 + y ** 2)

print (z)

#plot z 
plt.yticks(np.arange(5))
plt.imshow(z, cmap=plt.cm.gray);
plt.colorbar();
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()