try:
    print (0 / 0)
except ZeroDivisionError:
    #print ( "cannot divide by zero" )
    None

#List splice, assigning list = multiple variables
import sys
try:
    x = [1,2,3,4,5,6]
    print (x[-1::-1])
    x1,x2,x3,x4,x5,x6,x7 = x + [9]
    y = x1,x2,x3,x4,x5,x6,x7
    #x[8] = 4
    #print (x[8])
    print (x[-6:2])
    print (x7)
    print (y.count(0))

    print ( type( (y)) )
except:
    e = sys.exc_info()
    print ("An error Occured {} :- {}".format(e[0],e[1]))