#! usr/bin/env/python
'''
	Date,Open,High,Low,Close,Volume,Adj Close
	
	Bollinger Band
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


deviation = []
C = len(rev_c)

for i in range(N-1, C):
	if i + N < C:
		dev = rev_c[i: i+N]
	else:
		dev = rev_c[-N:]

	averages = np.zeros(N)
	averages.fill(sma[i - N -1])
	dev = dev - averages
	dev = dev ** 2
	dev = np.sqrt(np.mean(dev))
	deviation.append(dev)
	
deviation = 2 * np.array(deviation)
upperBB = sma + deviation
lowerBB = sma - deviation

t = np.arange(N-1, C)
plot(t, rev_c[N-1:], lw=1.0)
plot(t, sma, lw=2.0)
plot(t, upperBB, lw=3.0)
plot(t, lowerBB, lw=4.0)
show()