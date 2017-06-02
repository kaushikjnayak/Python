import pandas as pd
languages =  [ 'Mandarin ', 'Spanish', 'English', 'Hindi', 'Arabic', 'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Punjabi' ]

speakers = [ 955, 405, 360, 310, 295, 215, 205, 155, 125, 100 ]

#Create Pandas series from two arrays
spSer = pd.Series(speakers,index=languages, dtype = 'int64')

#construct a datframe from a Series oobject
spDatF = pd.DataFrame(spSer, columns = ['Speakers'])

#set the name of the index
spDatF.index.name = 'Languages'


print(spDatF)

