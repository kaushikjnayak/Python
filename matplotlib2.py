# Increase in Salary plotted across years 2009-2017
from matplotlib import pyplot as plt
import numpy as np

years = np.array([2009,2010,2011,2012,2013,2014,2015,2016,2017])

salary = np.array([0,320000,400000,480000,540000,820000,820000,1030000,1060000])


plt.title("Annual Gross Pay")
plt.ylabel("Rs")
plt.xlabel("Year")

my_xticks = years
plt.xticks(years, my_xticks)

plt.plot(years, salary, color='green', marker='o', linestyle='solid')
plt.show()


