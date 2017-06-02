K, M =  map(int,input().split())
S = 0
for i in range(K):
   S +=  max(list(map(int, input().split()[1:]))) ** 2

print (S % M)

from itertools import  product
K, M = map(int, input().split())
Fsum = []
for n in range(K):
    Fsum.append([int(i)**2 for i in (input().split())[1:]])
print(max([sum(i)%M for i in list(product(*Fsum))]))