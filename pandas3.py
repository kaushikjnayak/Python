__author__ = 'kaushik'

import pandas as pd

df = pd.read_csv( 'D:/KAUSHIK/kjn/workspace/Python/FILES/City_list_file.csv')

#print(df)
#print ( df['Population_2011'] > 5000000)



cols = ['No' ,'City' , 'Population_2011']

#print (df [cols] )

df = df.set_index(['State', 'City'])

print (df.loc['Maharashtra', 'Mumbai'])