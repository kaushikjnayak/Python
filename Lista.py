from itertools import combinations
N = int(input())
Al = input().split()
K = int(input())

NKcomb = list(combinations(range(1,N+1),K))

prob_of_a = sum([i + 1 == k[0] for k in NKcomb for i, j in enumerate(list(Al))  if j == 'a'])

print (  round(prob_of_a / len(NKcomb),4 ) )

