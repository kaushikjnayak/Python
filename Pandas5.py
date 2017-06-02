import pandas as pd
import numpy as np
# Read data from a csv file and store as a dataframe.
cities = pd.read_csv('D:/KAUSHIK/kjn/workspace/Python/FILES/City_list_file.csv')

#change the index from default index to city name
cities.set_index('City', inplace=1)
cities.index.name = 'City'

#Sort the index based on alphabetical order (reverse = 1 for rev alph order.
cities = cities.reindex(sorted(cities.index, reverse=0))
print (cities)

#drop the column No from the Dframe.
cities.drop(['No'],axis=1,inplace=True)

print(cities)