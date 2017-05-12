#Set opeartions
x = [1,2,3,4,5,6]


print (x[-1::-1])
print (x[0:-1]  )

y = set(x)

z = set([4,7,3])

print(z.difference(y))
print(y.union(z))
print(y.intersection(z))

print (y.issuperset(z))

z.remove(7)

print (z)
print (z.issubset(y))

z.pop()
print (z)

