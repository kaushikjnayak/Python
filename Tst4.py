def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    score_a = score_b = 0
    for i , j in zip ( [a0,a1,a2], [b0, b1, b2]):
        if i > j:
            score_a += 1
        elif j > i:
            score_b += 1
    return [score_a,score_b]

print (solve(5,6,7,6,6,10))