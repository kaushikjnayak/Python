#count the Number of digits and alphabets in a sentence
str1 = input ('Enter a Sentence: ')

characters = list(str(str1));
alcount = 0
dgcount = 0
for l in characters:
    if l.isalpha():
        alcount += 1
    if l.isdigit():
        dgcount += 1
print ("Letters = %d "  % alcount)
print ("Digits  = %d" % dgcount)
