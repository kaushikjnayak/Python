area = 1256.66
volume = 1254.725
decimals = 2
print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals = 3
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))


def vowcount(istr):
    vcount ={}
    for i in list(istr):
        for j in ('a','e', 'i','o', 'u'):
            if i == j:
                if i in vcount:
                 vcount[j] += 1
                else:
                 vcount[j] = 1
    for vow,ct in vcount.items():
        print ('Vowel -> {} | count -> {}'.format(vow,ct))

vowcount('Kaushikjnayak')

''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT
def main(num):
    # Write code here
    a = type(num)
    print("This input is of type {}.".format(a))


main(23)