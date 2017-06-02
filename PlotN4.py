import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


#using ticker to make standard ticks.

def gen_len_alpha( a , b):
    return '[{} , {}]'.format(b, int(a) / len(X) * 100 )


#setting the formatter for X - axis ticks.
ax = plt.axes()
ax.xaxis.set_major_formatter(ticker.FuncFormatter(gen_len_alpha))

X = [ 1, 2 , 3 , 4 ,5, 6 ,7,  8]

Y = np.cumsum(X)

print (Y)
plt.plot(X,Y,'k--')

plt.show()

