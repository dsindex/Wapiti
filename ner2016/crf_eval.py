#!/usr/bin/env python
#-*- coding: utf8 -*-

import os
from optparse import OptionParser

# global variable
VERBOSE = 0

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

number_of_sent = 0
number_of_success = 0
number_of_success_pos = 0
number_of_success_neg = 0
number_of_failure = 0
number_of_failure_pos = 0
number_of_failure_neg = 0

def spill(bucket) :
	'''
	0 : failure
	1 : success
	'''
	global number_of_sent
	global number_of_success
	global number_of_success_pos
	global number_of_success_neg
	global number_of_failure
	global number_of_failure_pos
	global number_of_failure_neg

	for line in bucket :
		try : 
			tokens = line.split('\t')
			answer = tokens[-3]
			predict = tokens[-2]
			predict_info = tokens[-1]
		except :
			sys.stderr.write("format error : %s\n" % (line))
			return 0
		if answer != 'O' and answer != 'I' : target = True
		else : target = False

		ct_score = float(predict_info.split('/')[1])

		if target :
			if answer == predict :
				number_of_success += 1
				number_of_success_pos += 1
			else :
				number_of_failure += 1
				number_of_failure_pos += 1
		else :
			if answer == predict :
				number_of_success += 1
				number_of_success_neg += 1
			else :
				number_of_failure += 1
				number_of_failure_neg += 1

		if answer == predict : print line + '\t' + 'SUCCESS'
		else : print line + '\t' + 'FAILURE'

	number_of_sent += 1

	print '\n',

	return 1

if __name__ == '__main__':

	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	(options, args) = parser.parse_args()

	bucket = []

	while 1:
		try:
			line = sys.stdin.readline()
		except KeyboardInterrupt:
			break
		if not line:
			break
		line = line.strip()
		if line and line[0] == '#' : continue

		if not line and len(bucket) >= 1 : 
			ret = spill(bucket)
			bucket = []
			continue

		if line : bucket.append(line)

	if len(bucket) != 0 :
		ret = spill(bucket)

	sys.stderr.write("number_of_sent = %d\n" % (number_of_sent))
	sys.stderr.write("number_of_success = %d\n" % (number_of_success))
	sys.stderr.write("number_of_success_pos = %d\n" % (number_of_success_pos))
	sys.stderr.write("number_of_success_neg = %d\n" % (number_of_success_neg))
	sys.stderr.write("number_of_failure = %d\n" % (number_of_failure))
	sys.stderr.write("number_of_failure_pos = %d\n" % (number_of_failure_pos))
	sys.stderr.write("number_of_failure_neg = %d\n" % (number_of_failure_neg))
	precision_pos = number_of_success_pos / float(number_of_success_pos + number_of_failure_pos)
	sys.stderr.write("precision(positive) = %f\n" % (precision_pos))
	precision_neg = number_of_success_neg / float(number_of_success_neg + number_of_failure_neg)
	sys.stderr.write("precision(negative) = %f\n" % (precision_neg))
	accuracy = (precision_pos + precision_neg) / 2
	sys.stderr.write("accuracy  = %f\n" % (accuracy))
