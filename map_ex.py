__author__ = 'kaushik'

ab = [ 'a0', 'b0', 'a1', 'b1']
db = [ 'd0', 'b0', 'd1', 'b1']

ab = [ 1,3,4 ]
db = [ 1,2,3 ]

ab = {1:2, 3:5, 1:67}
db = {1:3, 3:5, 2:6}

def chk(a,b):
    return a == b

print (list (map(chk,ab,db)))



people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1

list(map (split_title_and_name,people) ) ==   list(map(lambda person: person.split()[0] + ' ' + person.split()[-1] , people) )

#option 2
#list(map(split_title_and_name, people)) == list(map(???))
