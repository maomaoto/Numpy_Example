#! usr/bin/env/python
'''
	Data download from Yahoo Finance
	
	Date,Open,High,Low,Close,Volume,Adj Close
'''


import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = 8	# window size
weights = np.hanning(N)
print("Weights {0}".format(weights))

avgo = np.loadtxt('AVGO_clipped.csv', delimiter=',', usecols=(4,), unpack=True)
avgo = avgo[::-1]

qrvo = np.loadtxt('QRVO_clipped.csv', delimiter=',', usecols=(4,), unpack=True)
qrvo = qrvo[::-1]

# return
avgo_returns = np.diff(avgo)/avgo[:-1]
qrvo_returns = np.diff(qrvo)/qrvo[:-1]

# smooth
smooth_avgo = np.convolve(weights/weights.sum(), avgo_returns)[N-1:-N+1]
smooth_qrvo = np.convolve(weights/weights.sum(), qrvo_returns)[N-1:-N+1]

t = np.arange(N-1, len(avgo_returns))

plot(t, avgo_returns[N-1:], lw = 1.0)
plot(t, smooth_avgo, lw=2.0)
plot(t, qrvo_returns[N-1:], lw = 1.0)
plot(t, smooth_qrvo, lw = 2.0)
show()

K = 3
poly_avgo = np.polyfit(t, smooth_avgo, K)
poly_qrvo = np.polyfit(t, smooth_qrvo, K)

poly_sub = np.polysub(poly_avgo, poly_qrvo)

xpoints = np.roots(poly_sub)
print("Intersection points {0}".format(xpoints))

reals = np.isreal(xpoints)
print("Real number? {0}".format(reals))

xpoints = np.select([reals], [xpoints])
xpoints = xpoints.real
print("Real intersection points {0}".format(xpoints))

print("Sans 0s {0}".format(np.trim_zeros(xpoints)))