#! usr/bin/env/python
'''
	Date,Open,High,Low,Close,Volume,Adj Close
'''

import numpy as np
import sys

h, l, c = np.loadtxt('GOOG.csv', delimiter=',', usecols=(2,3,4), unpack=True)

N = int(sys.argv[1])
h = h[:N]
l = l[:N]
previousclose = c[1:N+1]

print('len(h) = {0}, len(l) = {1}'.format(len(h), len(l)))
print("len(previouseclose) = {0}".format(len(previousclose)))
print("Previouse close = {0}".format(previousclose))

truerange = np.maximum(h-l, h-previousclose, previousclose-l)

atr = np.zeros(N)
atr[-1] = np.mean(truerange)

for i in range(2, N+1):
	atr[-i] = (N-1) * atr[-i+1] + truerange[-i]
	atr[-i] /= N
	
print("ATR = {0}".format(atr))