__author__ = 'kaushik'


def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))

def reverse_string(text):
    return ''.join(reversed(text))

if False:
 print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
 print(reverse_string_words("Python Exercises."))


 print(reverse_string("The quick brown fox jumps over the lazy dog."))
 print(reverse_string("Python Exercises."))

def strip_chars(instr,schar):
    ostr = ''
    for i in list(instr):
        if i not in schar:
             ostr += i
    return ostr

a = strip_chars('Kaushik Leaves to work' , 'kt')

print (a)