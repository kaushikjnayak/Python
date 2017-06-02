def count_substring(string, sub_string):
    sublen = len(sub_string)
    ct = 0
    for i in range (len(string) - 1, -1, -1):
        if (string[i:-(sublen - i):-1]   ) == sub_string or ( string[i::-1]   ) == sub_string \
                or string[i]  == sub_string:
             ct += 1
    return ct

print (count_substring('12jlka445kljakldfjlaksjdfdka3942','3942'))


