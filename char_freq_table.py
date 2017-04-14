def char_freq_table(afilename):
    import os                                                 
    if not ( os.path.isfile(afilename) ):                     
       print ('File ',afilename,' does not exist')
       return
    char_freq = {}
    FILE = open(afilename,'r')
    for line in FILE:
        for c in list(line):
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1
                
    for ch in sorted(char_freq):
        print ("%s -> %d" % ( ch,char_freq[ch]))
    
char_freq_table('C:/Users/kaushik/Desktop/city.dmp')