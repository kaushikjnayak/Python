__author__ = 'kaushik'

import pandas as pd

df = pd.read_csv( 'D:/KAUSHIK/kjn/workspace/Python/FILES/City_list_file.csv' , index_col = 4)

#print ( df['Population_2011'] > 5000000)


a = [ 'Mumbai' , 'Bengaluru', 'Delhi', 'Chennai']

b = pd.Series(a)
b.loc[3] = 'Pune'
print (b)

print ( df.loc['Maharashtra'])

#print ( df.T)


print ( df[df['Population_2011']  > 10000000])


cols = ['No' ,'City' , 'Population_2011']

print (df [cols] )

df.reset_index()

df.set_index('State')