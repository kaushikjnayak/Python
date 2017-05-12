#Plot GDP of top 10 economies (2017)

from matplotlib import pyplot as plt
country = [ 'United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Brazil', 'Italy', 'Canada' ]

GDP = [ 19417.14, 11795.30, 4841.22, 3423.29, 2496.76, 2454.46, 2420.44, 2140.94, 1807.43, 1600.27 ]

ctrylen = [i + 0.1 for i,j in enumerate(country)]
plt.xlabel('Countries')
plt.ylabel('GDP Nominal (billions of $)')


plt.title('GDP of top 10 Economies in 2017')
plt.xticks([i + 0.5 for i,j in enumerate(country)],country)
plt.bar(ctrylen,GDP,color='green',  linestyle='solid')

plt.show()