__author__ = 'kaushik'

def front_back(str):
    if  len(str) <= 1:
       return str

    else:
       beg = str [0]
       end = str[len(str)-1]
       midd = str [1:len(str)-1]
       return end + midd + beg



print (front_back(''))