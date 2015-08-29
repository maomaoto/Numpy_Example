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

b = rev_c[-N:]
b = b[::-1]
print("b {0}".format(b))

A = np.zeros((N, N), float)
print("Zeros N by N {0}".format(A))

for i in range(N):
	A[i, ] = rev_c[-N-1-i:-1-i]
	
print("A {0}".format(A))

(x, residuals, rank, s) = np.linalg.lstsq(A, b)

print x, residuals, rank, s

print np.dot(b, x)