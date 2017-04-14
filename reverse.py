def reverse(str1):
    strlst = list(str1)
    newstr1 = ''
    strlen = len(str1)
    i = strlen - 1
    while (i >= 0 ):
        newstr1 += strlst[i]
        i -= 1
    return newstr1
        
