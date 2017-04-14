def len_of_words(alist):
    lenlist = []
    for i in alist:
        lenlist.append(len(i))
    return lenlist


print ( len_of_words(['78','90','78']));