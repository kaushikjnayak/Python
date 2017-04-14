def func1(a, *tup1, **dict1):
    return str(a) + '-' + str(tup1[0]) + '-' + str(dict1['first'])

str_a1   = 'KJN'
tup_a1   = ('Hello','KJN','HOW ARE YOU?')
dict_a1  = { 'first' :  'I', 'second' :  'II' }

print ( func1(str_a1,tup_a1,first =  'I', second =  'II'))
#print ( func1(str_a1,tup_a1,dict_a1))