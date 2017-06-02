n = int(input())
s = set(map(int, input().split()))

opcount = int(input())

funclist = { 'pop': s.pop,'remove': s.remove, 'discard':s.discard}
for i in range(opcount):
    op,*arg = input().split()
    if op in funclist:
       funclist[op](int(arg[0]))  if arg else funclist[op]()

print (sum(s))