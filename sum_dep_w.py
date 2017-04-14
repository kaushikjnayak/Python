print ('Enter Transactions')
total = 0
while True:
    strinp = input()
    if strinp:
        tran = strinp.split(' ')
        if tran[0] == 'D':
            total = total + int(tran[1])
        elif tran[0] == 'W':
            total = total - int(tran[1])
        else:
            print ("Invalid Transaction")

    else:
        break
print ("Print Total = %d" % total)
