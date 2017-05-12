import pandas as pd

languages =  [ 'Mandarin ', 'Spanish', 'English', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Punjabi' ]

speakers = [ 955, 405, 360, 310, 295, 215, 205, 155, 125, 100 ]

#Create Pandas series from two arrays
spDB = pd.Series(speakers,index=languages, dtype = 'int64')

print(spDB)

print (spDB[['Mandarin','English','Hindi']])


#create Series from Dictionary
nd = pd.Series( {'a':1, 'b':2})
print (nd)

#create Series from Dictionary using your own keys. missing values will be Na
nd = pd.Series( {'a':1, 'b':2, 'm' : 1} , index = ['m','n'])
print (nd)

#Check which values are Na
print (nd.isnull())

#In operator on series
print ('a' in nd)
