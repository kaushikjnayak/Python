import pandas as pd
import numpy as np
# Read data from a csv file and store as a dataframe.
cities = pd.read_csv('D:/KAUSHIK/kjn/workspace/Python/FILES/City_list_file.csv')

#change the index from default index to city name
cities.set_index('City', inplace=1)

print (cities)
