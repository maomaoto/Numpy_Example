#! usr/bin/env/python
'''
	Date,Open,High,Low,Close,Volume,Adj Close
	
	Simple moving average
'''

import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = int(sys.argv[1])

weights = np.ones(N)/N
print("Weights {0}".format(weights))

c = np.loadtxt('GOOG.csv', delimiter=',', usecols=(4,), unpack=True)
# reverse close array
rev_c = c[::-1]
sma = np.convolve(weights, rev_c)[N-1:-N+1]

t = np.arange(N-1, len(rev_c))
plot(t, rev_c[N-1:], lw=1.0)
plot(t, sma, lw=2.0)
show()

