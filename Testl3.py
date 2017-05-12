def swap_case(s):
    a = []
    for i in list(s):
        if i.lower() == i:
            a.append(i.upper())
        elif i.upper() == i:
            a.append(i.lower())
    return ''.join(a)

print (('HackerRank.com presents "Pythonist 2".').swapcase())

def split_and_join(line):
    # write your code here
    return '-'.join(line.split(' '))

print(split_and_join('hello there'))

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a,b))

print (print_full_name('Guido','Rossum'))

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
print(mutate_string('abracadabra',5,'k'))