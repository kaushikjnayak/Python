import numpy as np
import matplotlib.pyplot as plt

def pdf(X, mu, sigma):
  a = 1. / (sigma * np.sqrt(2. * np.pi))
  b = -1. / (2. * sigma ** 2)
  return a * np.exp(b * (X - mu) ** 2)

X = np.linspace(-6, 6, 1024)

plt.plot(X, pdf(X, 0., 1.),   color = 'k', linestyle = 'solid')
plt.plot(X, pdf(X, 0.,  .5),  color = 'k', linestyle = 'dashed')
plt.plot(X, pdf(X, 0.,  .25), color = 'k', linestyle = 'dashdot')

plt.show()


N = 8
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)

plt.bar(X, A, color = 'w', hatch = '-')
plt.bar(X, A + B, bottom = A, color = 'w', hatch = '+')

plt.show()