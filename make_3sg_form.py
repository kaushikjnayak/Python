def make_3sg_form(astr):
    newstr = ''
    import re
    if astr.endswith("y"):
       newstr = re.sub(r'y$','ies',astr)
    elif astr.endswith("o") or astr.endswith("ch") or astr.endswith("s") or astr.endswith("sh") or astr.endswith("x") or astr.endswith("z"):
         newstr = re.sub(r'$','es',astr)
    else:
        newstr = re.sub(r'$','s',astr)
    return newstr
    

print (make_3sg_form('enemy'))
print (make_3sg_form('inch'))