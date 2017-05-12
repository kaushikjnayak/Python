with open('D:\KAUSHIK\kjn\ebooks\imp_links.txt') as filein, open('D:\KAUSHIK\kjn\ebooks\imp_links.log','a') as fileout:
       fileout.write(filein.read())

for line in  open('D:\KAUSHIK\kjn\ebooks\imp_links.log'):
    print (line)