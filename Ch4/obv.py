#! usr/bin/env/python
'''
	Data download from Yahoo Finance
	
	Date,Open,High,Low,Close,Volume,Adj Close
'''


import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show


def datestr2num(s):
	'''
		0 - Monday
		6 - Sunday
	'''
	return datetime.datetime.strptime(s, "%Y-%m-%d").date().weekday()

c, v = np.loadtxt('AVGO_clipped.csv', delimiter=',', usecols=(4,5), unpack=True)
c = c[::-1]
v = v[::-1]

change = np.diff(c)
print("Change {0}".format(change))

signs = np.sign(change)
print("Signs {0}".format(signs))

pieces = np.piecewise(change, [change <0, change >0], [-1, 1])
print("Pieces {0}".format(pieces))

print("Arrays equal? {0}".format(np.array_equal(signs, pieces)))

print("On balance volume {0}".format(v[1:] * signs))