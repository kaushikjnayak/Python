n = int(input())

primary = []
for i in range(n):
    primary.append(input())

q = int(input())

for i in range(q):
 inp = input()
 print ( sum([ inp == j for j in primary ]))
