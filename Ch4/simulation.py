#! usr/bin/env/python
'''
	Data download from Yahoo Finance
	
	Date,Open,High,Low,Close,Volume,Adj Close
'''


import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show


def calc_profit(open, high, low, close):
	# buy at a price slightly lower than open
	buy = open * float(sys.argv[1])
	print(buy)
	# daily range
	if low < buy < high:
		return (close - buy) / buy
	else:
		return 0
	
	
o, h, l, c = np.loadtxt('AVGO_clipped.csv', delimiter=',', usecols=(1, 2, 3, 4), unpack=True)
o = o[::-1]
h = h[::-1]
l = l[::-1]
c = c[::-1]

func = np.vectorize(calc_profit)

profits = func(o, h, l, c)
print("Profits {0}".format(profits))

real_trades = profits[profits != 0]
print("Number of trades {0} {1}%".format(len(real_trades), round(100.0 * len(real_trades) / len(c), 2)))
print("Average profit/loss {0}%".format(round(np.mean(real_trades) * 100.0, 2)))

winning_trades = profits[profits > 0]
print("Number of winning trades {0} {1}%".format(len(winning_trades), round(100.0 * len(winning_trades) / len(c), 2)))
print("Average profit {0}%".format(round(np.mean(winning_trades) * 100.0, 2)))

losing_trades = profits[profits < 0]
print("Number of winning trades {0} {1}%".format(len(losing_trades), round(100.0 * len(losing_trades) / len(c), 2)))
print("Average profit {0}%".format(round(np.mean(losing_trades) * 100.0, 2)))
