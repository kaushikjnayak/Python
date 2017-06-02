import pandas as pd
import numpy as np
# Read data from a csv file and store as a dataframe.
cities = pd.read_csv('D:/KAUSHIK/kjn/workspace/Python/FILES/City_list_file.csv')

#change the index from default index to city name
cities.set_index('City', inplace=1)

print (cities)
print (cities.columns)

#construct a dataframe from a dictionary. Include another column Description with columns=
mycities = pd.DataFrame({'City' : [ 'Mangalore','Bhubaneshwar', 'Kundapaura', 'Mumbai'],
                         'State' : [ 'Karnataka','Odisha','Karnataka','Maharashtra']}, columns=['City','State', 'Description'])
print (mycities)

# get a record at a specific index location
print (cities.loc['Bangalore'])

# fetch all the state column
print (mycities['State'])

# Change the value of a particular column value
mycities['Description'] =  np.arange(4)
mycities['Description'] =  np.arange(4)

#access a particular column from . operator
print (mycities.City)

#get all the cities that startswith
print ( mycities.where(mycities.City.str.startswith('K')))

#Data frame with all cities that start with'M'
print ( cities[(cities['State'].str.startswith('M'))])

cities['Metro'] = cities.Population_2011 >= 10000000

cities.columns.name = 'All Cities'
print (cities.columns)

#return cities as 2d  ndarray
print (cities.values)

mycities.set_index('City', inplace=1)

