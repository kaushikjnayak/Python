import matplotlib.pyplot as plt

import numpy  as np


fig = plt.figure()

ax = fig.add_subplot(1,1,1)

#Plot 200 Random numbers
ax.plot(np.random.randn(200).cumsum())

ticks = ax.set_xticks([0,40,80,160,200])

xticklabels = ax.set_xticklabels(['FIRST','SECOND','THIRD','FOURTH','FIFTH'])

ax.set_title('CUMULATIVE SUM OF RANDOM NUMBERS ')

ax.set_xlabel('LEVELs')

ax.set_ylabel('NUMBERS')

plt.show()