#lambda,  filter, map(), reduce()

arr1 = [23, 56, 78, 90]

def retfunc(n):
    return lambda x : x * 2 * n

f1 = retfunc(2)
f2 = retfunc(3)
f3 = retfunc(4)

print("f1(5) = {},f2(5) = {},f3(5) = {}".format(f1(5),f2(5),f3(5)))

import math
alist1 = list(map(math.sin, arr1))

print (alist1)

alist2 = list(  map(lambda x : x ** 2, arr1) )

print (alist2)


alist3 = list( filter(lambda x : x % 2 == 0, arr1))

print (alist3)

import functools as f
alist4 =  f.reduce( (lambda x,y : x  * y * 2 ), arr1)

print (alist4)


import collections as col

c = col.defaultdict()

c[7] = 9

#get function of dict obj works like sql Nvl( mysql ifnull)  except that first argument is checked for not defined
#instead of not null .
print (c.get(8, 56))


# Get word count of a long paragraph. consider for additional characters like <tabs> , , . ; etc
def wordcount(document):
 import re
 word_counts = {}
 for word in re.split("[\n\.,;\'\": ]+",document):
    try:
        if word.strip():
           word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1
#Alphabetical order of the words
 #return sorted( word_counts.items(),key=lambda x: str.lower(x[0]))

#Sorted based on Word frequency High->low .
 return sorted( word_counts.items(),key=lambda x: x[1],reverse=1)

a = wordcount('''At some point, you may need to break a large string down into smaller chunks, or strings. This is the opposite of concatenation which merges or combines strings into one.

To do this, you use the split function. What it does is split or breakup a string and add the data to a string array using a defined separator.

If no separator is defined when you call upon the be function,    itemspace will be used by default. In simpler terms, the separator is a defined character that will be placed between each variable.
''')

for i in a:
    print (i)