#! usr/bin/env/python
'''
	Data download from Yahoo Finance
	
	Date,Open,High,Low,Close,Volume,Adj Close
'''


import numpy as np
import datetime

def datestr2num(s):
	'''
		0 - Monday
		6 - Sunday
	'''
	return datetime.datetime.strptime(s, "%Y-%m-%d").date().weekday()

c = np.loadtxt('GOOG.csv', delimiter=',', usecols=(4,), unpack=True)

# median
print("median = {0}".format(np.median(c)))

sorted_close = np.msort(c)
#print("sorted = {0}".format(sorted_close))
N = len(c)
print("middle = {0}".format(sorted_close[N/2]))
print("averaged middle = {0}".format((sorted_close[N/2]+sorted_close[(N-1)/2])/2))

# variance
print("variance = {0}".format(np.var(c)))

print("variance from definition = {0}".format(np.mean((c - c.mean()) ** 2)))

# return

returns = np.diff(c)/c[:-1]
print("Returns")
print("Standard deviation = {0}".format(np.std(returns)))

logreturns = np.diff(np.log(c))
print("log returns: {0}".format(logreturns))

posretindices = np.where(returns > 0)
print("Indices with positive returns: {0}".format(posretindices))

# volatility

annual_volatility = np.std(logreturns)/np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1./252.)
print("annual volatility = {0}".format(annual_volatility))
print("monthly volatility = {0}".format(annual_volatility * np.sqrt(1./12.)))

print(datestr2num("2015-08-30"))


# dates
dates, close = np.loadtxt('GOOG.csv', delimiter=',', usecols=(0,4), converters={0:datestr2num}, unpack=True)
print("Dates = {0}".format(dates))
averages = np.zeros(5)

for i in range(5):
	indices = np.where(dates == i)
	prices = np.take(close, indices)
	avg = np.mean(prices)
	print("Day {0}, prices: {1}, Average: {2}".format(i, prices, avg))
	print("Day {0}, Average: {1}".format(i, avg))
	averages[i] = avg
	
top = np.max(averages)
print("Highest average = {0}".format(top))
print("Top day of the week = {0}".format(np.argmax(averages)))
bottom = np.min(averages)
print("Lowest average = {0}".format(bottom))
print("Bottom day of the week = {0}".format(np.argmin(averages)))