import matplotlib.pyplot as plt

import numpy as np
fig = plt.figure()
ax1 = fig.add_subplot(1, 3, 1)
plt.show()

plt.plot(np.random.randn(50).cumsum(), 'k--')

plt.show()


fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i, j].hist(np.random.randn(500), bins=50, color='k', alpha=0.5)
plt.subplots_adjust()
plt.show()