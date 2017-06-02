#for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
  #  a = int(input()); A = set(input().split())
   # b = int(input()); B = set(input().split())
    #print ( True if len( A.difference(B)) == 0 else False)


A = set([1,2,3])
B = set([1,2,4])



A =  set(list(map(int,input().split())))

n = int(input())

T = []
for i in range(n):
    B = set(list(map(int,input().split())))
    T.append(  A.issuperset(B) and A != B  )
print (all(T))