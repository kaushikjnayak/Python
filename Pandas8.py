import pandas as pd
import numpy as np

employees = pd.read_csv('C:/Users/kaushik/PycharmProjects/PRJ_2/EMPLOYEES.csv')
departments = pd.read_csv('C:/Users/kaushik/PycharmProjects/PRJ_2/DEPARTMENTS.csv')


print (employees)

#Give a salary hike of 25% to all employees
employees['SALARY'] = employees['SALARY'].apply(lambda x : x * 1.25)

#Employees with salay < 10000
employees[employees['SALARY'] > 10000]

#details of employee with a Minimum salary among  salaries > 10000
employees[employees['SALARY'] > 10000].min()

#Display columns in sorted (descending in this case) order
employees.sort_index(axis = 1, ascending = False)

#Order employes by decreasing salaries
employees.sort_values(by='SALARY', ascending = False)


#Rank Salaries and append it as a new column
employees['RANK'] = employees['SALARY'].rank() #Defalut is by weigthed average
employees['RANK'] = employees['SALARY'].rank(method = 'first') # order of appearance
employees['RANK'] = employees['SALARY'].rank(method = 'min') # In a series [1,2 3,3,5] 3 and 3 are ranked 3, 5 is ranked 5
employees['RANK'] = employees['SALARY'].rank(method = 'max') # In a series [1,2 3,3,5] 3 and 3 are ranked 4, 5 is ranked 5
employees['RANK'] = employees['SALARY'].rank(method = 'max') # In a series [1,2 3,3,5] 3 and 3 are 3, 5 is ranked 4

#Sort the entire dataframe by rank ( new column )
employees.sort_values(by='RANK', ascending = False)

import datetime

