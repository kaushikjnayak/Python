__author__ = 'kaushik'

import pandas as pd


Indvillages = pd.Series({'Name': 'Basrur', 'pop' : 3000 ,  'nearby' : 'kandlur'  , 'HQ' : 'kundapura'})

Indtowns = pd.Series({'Name' : 'Kundapura', 'pop' : 50000, 'nearby' : 'Udupi' , 'HQ'  : 'Udupi' })

Indcity1 = pd.Series({'Name' : 'Mangalore' ,'pop' : 500000, 'nearby' : 'Udupi' , 'HQ'  : ''})

Indcity2 = pd.Series({'Name' : 'Mumbai' ,'pop' : 12000000, 'nearby' : 'Pune' , 'HQ'  : 'Maharshtra'})


df = pd.DataFrame( [ Indcity1,Indcity2,Indtowns,Indvillages ]  , index = [ 'city' , 'city' , 'town' , 'village'] )

print (df.loc['town' , 'HQ'])

#print (df.T)

df['State'] = None
print (df.loc['city', 'State' ] )
print (df)


