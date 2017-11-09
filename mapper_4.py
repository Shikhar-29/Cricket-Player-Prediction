#!/usr/bin/python

import sys


full = sys.stdin

for line in full:
	data = line.strip().split(',')
	result = data[4].strip() + ',' + data[8].strip() + ',' + data[10].strip()
	print '{0}\t{1}'.format(data[0], result)

