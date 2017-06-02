#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

prisum = 0
secsum = 0

for i,row in enumerate(a):
    prisum += row[i]
    secsum += row[n-1-i]

print (abs(prisum - secsum ))
