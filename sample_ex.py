__author__ = 'kaushik'


print ("""Here is a line
"another line"
another line
'another line
'last line
"""
)

import datetime

dt1 = datetime.datetime.strptime('2017-04-09','%Y-%m-%d')
dt2 = datetime.datetime.strptime('2017-04-17','%Y-%m-%d')


dt_diff =  (  (dt2 - dt1).days )
print ("Date difference - " + str(dt_diff) + " day(s)")

for i in range(3,59):
    print (i)


lstr = input("Enter a string")

if lstr.startswith('ls'):
    tstr = lstr
else:
    tstr = "ls" + lstr

print (tstr)


stroup = ""
strinp = input('Enter a string:')
n = input('Enter a number n:')
if n.isnumeric():
     for i in range(1,int(n)):
         stroup = stroup + strinp
print ( stroup )

a = [ 4,6,7,8,9,0,56,89]

print (a.count(4))
