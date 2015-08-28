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

def summarize(a, o, h, l, c):
	monday_open = o[a[-1]]
	week_high = np.max(np.take(h, a))
	week_low = np.min(np.take(l, a))
	friday_close = c[a[0]]
	
	return ("GOOG", monday_open, week_high, week_low, friday_close)

# dates
dates, open, high, low, close = np.loadtxt('GOOG.csv', delimiter=',', usecols=(0,1,2,3,4), converters={0:datestr2num}, unpack=True)

# consider last 3wks for concept
close = close[:20]
dates = dates[:20]

# Because data is in descendant order
# Find first Friday
first_friday = np.ravel(np.where(dates == 4))[0]
print("The first Friday index is {0}".format(first_friday))

# find last Monday
last_monday = np.ravel(np.where(dates == 0))[-1]
print("The last Monday index is {0}".format(last_monday))

# index for these 3 weeks
weeks_indices = np.arange(first_friday, last_monday +1)
print("Weeks indices initial {0}".format(weeks_indices))

weeks_indices = np.split(weeks_indices, 3)
print("Weeks indices after split {0}".format(weeks_indices))

weeksummary = np.apply_along_axis(summarize, 1, weeks_indices, open, high, low, close)
print("Week summary: {0}".format(weeksummary))

np.savetxt("Weeksummary.csv", weeksummary, delimiter=",", fmt="%s")