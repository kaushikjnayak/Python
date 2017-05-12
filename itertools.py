import itertools as it

#Iterate through the entire list , then through the characters

a = ['kaushik','nayak', '1234']
b = [('kaushik'),('nayak','abcd'), ['1234']]

for i in it.chain(*a):
 print (i)


for i in it.chain(*b):
    print (i)


#List grouped by length of each element.
f = lambda a : len(a)


for i,j in it.groupby(a,f):
    print (i,list(j))


# Display all permutations of list a
for i in it.permutations(a):
    print (i)