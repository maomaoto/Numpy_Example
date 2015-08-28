#! usr/bin/env/python
'''
	Data download from Yahoo Finance
	
	Date,Open,High,Low,Close,Volume,Adj Close
'''


import numpy as np

c,v = np.loadtxt('GOOG.csv', delimiter=',', usecols=(4,5), unpack=True)

# Volume-Weighted Average Price
vwap = np.average(c, weights=v)
print("VWAP = {0}".format(vwap))

# Mean
print("mean = {0}".format(np.mean(c)))

# Time-Weighted Average Price
# Just for demo, not practical 
t = np.arange(len(c))
print("TWAP = {0}".format(np.average(c, weights=t)))

# Max, min
h, l = np.loadtxt('GOOG.csv', delimiter=',', usecols=(2,3), unpack=True)
print("Highest = {0}".format(np.max(h)))
print("Lowest = {0}".format(np.min(l)))

# Spread
print("Spread high price {0}".format(np.ptp(h)))
print("Spread low price {0}".format(np.ptp(l)))