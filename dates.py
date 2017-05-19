__author__ = 'kaushik'

import datetime, time

#Display time
print(datetime.datetime.fromtimestamp(time.time()))

#get user input
dti = input("DDMMYYYY ?")

#convert user input to date.
dt = datetime.datetime.strptime(dti,"%d%m%Y")
print (dt)
