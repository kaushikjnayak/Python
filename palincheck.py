def palin_check_f(afilename):
    from reverse import reverse
    import os
    if not ( os.path.isfile(afilename) ):
        print 'File {0} does not exists'.format(afilename)
        return

    FILE = open(afilename,'r')
    for line in FILE:
        if reverse(line).rstrip('\n') == line.rstrip('\n'):
            print line
            
