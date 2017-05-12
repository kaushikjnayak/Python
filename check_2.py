__author__ = 'kaushik'

def check_vowel (inpstr):
        if list(inpstr)[0] in ( 'a','e', 'i' , 'o' , 'u'):
               print ("vowel")



list1 = [ 8,9,0,'abc']

if list1.__contains__('abc'):
    print ("present")


check_vowel('india')


def merge_str():
 stro = ''
 for i in  (['a', 'k', 'l', 'o', 'p' ]):
     stro = stro + i
 return stro



def histogram (alist):
    for num in alist:
            hist = ''
            for i in range(0,num):
              hist = hist + '*'
            print(hist)

print( histogram([1,2,3,4,5,6,7,8,9]) )

import csv

with open('D:/KAUSHIK/kjn/workspace/Python/FILES/test1.csv','r') as csvfile:
    d = list(csv.DictReader(csvfile))
for i,j in  d[1].items():
          print (i+" => "+j)



def gcd(a,b):

         rem = None

         if a >= b:
                  divd = a
                  divr = b
         else:
                  divd = b
                  divr = a

         while ( rem != 0 ):
                (quo,rem) = divmod(divd,divr)
                divd = divr
                divr = rem
         return divd



print ( gcd(180000,45))