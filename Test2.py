dct1  = dict.fromkeys([ 'a', 'b' , 'c' ])

print (dct1)


a = [ True, False, True, False, True ]

#sum of True
print (sum(a))

#sum of  elements > 3
num  = [ 1, 2 , 4 ,5 ]
print (sum (  [  b>3 for b in num ]))

ns = set(num)

print ( set(ns).union(ns))