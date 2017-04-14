
def ispangram(astr):
    alcount = {}
    wlist = [ c.lower() for c in list(astr) if c.isalpha() ]
    for c in wlist:
        if c in alcount:
           alcount[c] += 1
        else:
           alcount[c] = 1
         
    flag = 1
    for alph in list('abcdefghijklmnopqrstuvwxyz'):
        if not alph in alcount:
           flag = 0
           break

    if flag == 1:
        return True
    else:
        return False


print ( ispangram('kaushik'));
print ( ispangram('The quick brown fox jumps over the lazy dog'));

print ( ispangram('We promptly judged antique ivory buckles for the next prize'));

    
