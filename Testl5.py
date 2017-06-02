from  functools import reduce
s = 'sqA'
funclist = [ str.isalnum ,str.isalpha , str.isdigit, str.islower , str.isupper ]
x=32
y=5
print (x if x%4 == 0 else y)

print ( '-'.join(['1','2']))
print ( '1-2'.split('-'))