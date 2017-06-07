from  math import sqrt
from itertools import combinations

#Pythagorean triplet - a^2 + b^2 = c^2 for (a,b) <= (1999,1999)
def gen_pyth(n):
  if n >= 2000 :
      return
  ELEM =   [  [ i,j,i*i + j*j ] for i , j in list(combinations(range(1, n + 1 ), 2)) if sqrt(i*i + j*j).is_integer() ]
  print (*ELEM , sep = "\n")


gen_pyth(1999)
