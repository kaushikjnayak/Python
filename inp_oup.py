__author__ = 'kaushik'

#rad = input("Enter the radius")
import math
#rad = int(rad)
#print (rad * rad * math.pi)

#fname = input("Enter Fname")
#lname = input("Enter lname")

#print ("welcome "+ lname + ","+ fname)

seqinp = input ( "Enter list of numbers comma separated")

numarray = []
for n in (seqinp.split(',')):
    if n.isnumeric():
        numarray.append(n)
    else:
        print (n + " is not Numeric")

print (numarray)