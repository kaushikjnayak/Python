__author__ = 'kaushik'
from collections import defaultdict
salaries_and_tenures = [(83000, 8.7,35), (88000, 8.1,None),
                        (48000, 0.7,None), (76000, 6,None),
                        (69000, 6.5,None), (76000, 7.5,None),
                        (60000, 2.5,None), (83000, 10,None),
                        (48000, 1.9,None), (63000, 4.2,None)]

for salary,tenure,age in salaries_and_tenures:
    print("salary = {} tenure = {} age = {} ".format(salary,tenure,age))


abc = defaultdict(list)

abc = { salaries_and_tenures[i][1] : salaries_and_tenures[i] for i in range(len(salaries_and_tenures))
          }

print(abc)

dem = defaultdict(list)

dem['kaushik'].append('putta')
dem['kaushik'].append('kjn')
dem['Karthik'].append('kattiga')

print (dem )

import IPython as ip

import IPython as ip

print (1 + 1e2j)


print ('''  Kaushik .
This is not far . I Did not like this''')