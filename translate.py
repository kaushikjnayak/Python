def translate(str):
    nstr = ''
    strlst = list(str)

    for c in strlst:
        if c in ('a','e','i','o','u',' '):
            nstr += c
        else:
            nstr += c + 'o' + c
    return nstr
            
