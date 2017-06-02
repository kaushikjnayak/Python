def is_vowelword(word):
    all_vowels = 'aeiouAEIOU'
    return word[0] in all_vowels

def minion_game(string):
    # your code goes here
    words_stuart = {}
    words_kevin = {}
    for i,j in enumerate(string):
        word = j
        if is_vowelword(word):
           if word in words_kevin:
              words_kevin[word] += 1
           else:
               words_kevin[word] = 1
        else:
            if word in words_stuart:
               words_stuart[word] += 1
            else:
               words_stuart[word] = 1

        for m,n in enumerate(string[i+1:]):
          word += n
          if is_vowelword(word):
            if word in words_kevin:
              words_kevin[word] += 1
            else:
               words_kevin[word] = 1
          else:
            if word in words_stuart:
               words_stuart[word] += 1
            else:
               words_stuart[word] = 1
    if sum(words_stuart.values()) > sum(words_kevin.values()):
        print ('Stuart {}'.format(sum(words_stuart.values()) ) )
    elif sum(words_kevin.values()) > sum(words_stuart.values()):
        print('Kevin {}'.format(sum(words_kevin.values())))
    else:
        print ('Draw')
minion_game('BananA')


