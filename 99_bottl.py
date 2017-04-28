#The lyrics to the song 99 Bottles of Beer
String_orig = '''{0} bottles of beer on the wall, {0} bottles of beer.
Take one down, pass it around, {1} bottles of beer on the wall'''

count = 99
while  (count > 0):

    print String_orig.format(count,count - 1)
    count -= 1


    
