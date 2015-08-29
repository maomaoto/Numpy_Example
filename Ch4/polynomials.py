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

avgo = np.loadtxt('AVGO_clipped.csv', delimiter=',', usecols=(4,), unpack=True)
avgo = avgo[::-1]

qrvo = np.loadtxt('QRVO_clipped.csv', delimiter=',', usecols=(4,), unpack=True)
qrvo = qrvo[::-1]

t = np.arange(len(avgo))

poly = np.polyfit(t, avgo - qrvo, int(sys.argv[1]))
print("Polynomial fit {0}".format(poly))

print("Next value {0}".format(np.polyval(poly, t[-1]+1)))

print("Roots {0}".format(np.roots(poly)))

der = np.polyder(poly)
print("Derivative {0}".format(der))

print("Extremas {0}".format(np.roots(der)))

# double check
vals = np.polyval(poly, t)
print("np.argmax {0}".format(np.argmax(vals)))
print("np.argmin {0}".format(np.argmin(vals)))

plot(t, avgo - qrvo)
plot(t, vals)
show()