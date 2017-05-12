__author__ = 'kaushik'

a = [2,4,5,6,7,6]
s=1
for i in set(a):
    if type(i) == int:
        s *= i
print (s)
print (min(a))
print (7 in a)

array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
print(array)

import this

print ( a + a)