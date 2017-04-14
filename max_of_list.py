def max_of_list(alist):
    maxval = alist[0]
    for i in alist:
        if i > maxval:
            maxval = i
    return maxval
