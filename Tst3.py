__author__ = 'kaushik'

def wordocc ( sentence):
    words =  sentence.split(' ')
    print ("sentence : {}".format(sentence))

    for word in sorted(set ( words)):
        print ( "word {} , count = {}" . format(word,words.count(word)))


wordocc('''The method split() returns a list of all the words in the string, using str as the separator
        (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.''')


print ( 'a' in {'a':1, 'b':2})
print ( 'a' in ['a', 'b'])