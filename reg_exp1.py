def getnamFromEmail(emailid):
    import re
    matched = re.search('(.*)@.*\.com',emailid)
    if (matched):
     name = matched.group(1)
     print ('name = %s' %name)
    else:
     print 'Invalid Email id'
