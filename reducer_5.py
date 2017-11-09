#!/usr/bin/python

import sys


oldKey = None
sumGY = 0
sumGN = 0
py = 0
pn = 0
yes = 37.0
no = 1030.0
'''
for line in sys.stdin:
	data = line.strip().split('\t')
	key = data[0]
	value = data[1]
	if(data[0]=="AMRahane")
		print data,"**"
'''
for line in sys.stdin:

	key, value = line.strip().split('\t')
	if len(value.split(',')) == 3:
		_wickets, ground, status = value.split(',')
		wickets = float(_wickets)
		if oldKey and oldKey != key:
			pgy = sumGY/yes
			pgn = sumGN/no
			if pgy == 0:
				py = yes/(yes+no+2)
				pn = no/(yes+no+2)
			else:
				py = pgy*(yes)/(yes+no)
				pn = pgn*(no)/(yes+no)
				py=format(py,'.09f')
				print "{0}\t{1}\t{2}".format(oldKey, py, sumGY)
			oldKey = key
			py = 0
			pn = 0
			sumGY = 0
			sumGN = 0
		oldKey = key
		if ground == "Nagpur" and status == "yes":
			sumGY += 1
		elif ground == "Nagpur" and status == "no":
			sumGN += 1

