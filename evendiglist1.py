evenlist = []

for num in range(2400,3400):
    nlist = list(str(num))
    ctdig = len(nlist)
    ct = 0
    for dig in nlist:
        if int(dig)%2 == 0:
            ct += 1
    if ct == ctdig:
        evenlist.append(num)
        print(num)
