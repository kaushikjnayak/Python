import matplotlib.pyplot as plt
import pandas as pd

employees = pd.read_csv('employees.csv')
departments = pd.read_csv('departments.csv')

dep = employees['DEPARTMENT_ID'][1:20]
empsal = employees['SALARY'][1:20]

#barchart of salaries compared across departments
plt.bar(dep,empsal,height=5)

#display
plt.show()
