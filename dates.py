__author__ = 'kaushik'

import datetime, time

print(datetime.datetime.fromtimestamp(time.time()))

dti = input("DDMMYYYY ?")

dt = datetime.datetime.strptime(dti,"%d%m%Y")
print (dt)
