n_a = int(input())
list_a = map(int, input().split())

n_b = int(input())
list_b = map(int, input().split())

set_a = set(list_a)
set_b = set(list_b)


for i in set_a.symmetric_difference(set_b):
    print (i)


import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

sum = 0
for i in arr:
    sum += i
print (sum)