n1 = int(input())

A = set ( list( map(int, input().split())))

n2 = int(input())


for i in range(n2):
    oparg = input().split()
    func,argnum = oparg[0], int(oparg[1])
    B = set ( list( map(int, input().split())))
    if func == 'update':
        A.update(B)
    if func == 'intersection_update':
        A.intersection_update(B)
    if func == 'difference_update':
        A.difference_update(B)
    if func == 'symmetric_difference_update':
        A.symmetric_difference_update(B)

print (sum(list(A)))