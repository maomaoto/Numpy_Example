#! usr/bin/env/python
'''
	Data download from Yahoo Finance
	
	Date,Open,High,Low,Close,Volume,Adj Close
'''


import numpy as np
import datetime
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

# return

avgo_returns = np.diff(avgo)/avgo[:-1]
qrvo_returns = np.diff(qrvo)/qrvo[:-1]

# covariance matrix
covariance = np.cov(avgo_returns, qrvo_returns)
print("Covariance {0}".format(covariance))

# covariance diagonal
print("Covariance diagonal {0}".format(covariance.diagonal()))

# covariance trace
print("Covariance trace {0}".format(covariance.trace()))

# correlation
print("correlation")
print(covariance/(avgo_returns.std(ddof=1) * qrvo_returns.std(ddof=1)))
print("Correlation coefficient {0}".format(np.corrcoef(avgo_returns, qrvo_returns)))

# 同步
difference = avgo - qrvo
avg = np.mean(difference)
dev = np.std(difference)
print("Out of sync {0}".format(np.abs(difference[-1] - avg ) > 2 * dev))

t = np.arange(len(avgo_returns))
plot(t, avgo_returns, lw=1)
plot(t, qrvo_returns, lw=2)
show()