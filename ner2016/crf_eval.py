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
number_of_success_pos_rc = 0
number_of_success_neg_rc = 0
number_of_success_pos_pc = 0
number_of_success_neg_pc = 0
number_of_failure = 0
number_of_failure_pos_rc = 0
number_of_failure_neg_rc = 0
number_of_failure_pos_pc = 0
number_of_failure_neg_pc = 0

def spill(bucket) :
	'''
	0 : failure
	1 : success
	'''
	global number_of_sent
	global number_of_success
	global number_of_success_pos_rc
	global number_of_success_neg_rc
	global number_of_success_pos_pc
	global number_of_success_neg_pc
	global number_of_failure
	global number_of_failure_pos_rc
	global number_of_failure_neg_rc
	global number_of_failure_pos_pc
	global number_of_failure_neg_pc

	for line in bucket :
		try : 
			tokens = line.split('\t')
			answer = tokens[-3]
			predict = tokens[-2]
			predict_info = tokens[-1]
		except :
			sys.stderr.write("format error : %s\n" % (line))
			return 0

		ct_score = float(predict_info.split('/')[1])
		# recall
		if answer != 'O' :
			if answer == predict :
				number_of_success += 1
				number_of_success_pos_rc += 1
			else :
				number_of_failure += 1
				number_of_failure_pos_rc += 1
		else :
			if answer == predict :
				number_of_success += 1
				number_of_success_neg_rc += 1
			else :
				number_of_failure += 1
				number_of_failure_neg_rc += 1
		# precision
		if predict != 'O' :
			if predict == answer :
				number_of_success_pos_pc += 1
			else :
				number_of_failure_pos_pc += 1
		else :
			if predict == answer :
				number_of_success_neg_pc += 1
			else :
				number_of_failure_neg_pc += 1

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
	sys.stderr.write("number_of_failure = %d\n" % (number_of_failure))
	sys.stderr.write("number_of_success_pos_rc = %d\n" % (number_of_success_pos_rc))
	sys.stderr.write("number_of_failure_pos_rc = %d\n" % (number_of_failure_pos_rc))
	sys.stderr.write("number_of_success_neg_rc = %d\n" % (number_of_success_neg_rc))
	sys.stderr.write("number_of_failure_neg_rc = %d\n" % (number_of_failure_neg_rc))
	sys.stderr.write("number_of_success_pos_pc = %d\n" % (number_of_success_pos_pc))
	sys.stderr.write("number_of_success_neg_pc = %d\n" % (number_of_success_neg_pc))
	sys.stderr.write("number_of_failure_pos_pc = %d\n" % (number_of_failure_pos_pc))
	sys.stderr.write("number_of_failure_neg_pc = %d\n" % (number_of_failure_neg_pc))
	recall_pos = number_of_success_pos_rc / float(number_of_success_pos_rc + number_of_failure_pos_rc)
	sys.stderr.write("recall(positive) = %f\n" % (recall_pos))
	recall_neg = number_of_success_neg_rc / float(number_of_success_neg_rc + number_of_failure_neg_rc)
	sys.stderr.write("recall(negative) = %f\n" % (recall_neg))
	precision_pos = number_of_success_pos_pc / float(number_of_success_pos_pc + number_of_failure_pos_pc)
	sys.stderr.write("precision(positive) = %f\n" % (precision_pos))
	precision_neg = number_of_success_neg_pc / float(number_of_success_neg_pc + number_of_failure_neg_pc)
	sys.stderr.write("precision(negative) = %f\n" % (precision_neg))
	accuracy = (precision_pos + precision_neg) / 2
	sys.stderr.write("accuracy  = %f\n" % (accuracy))
	fmeasure_pos = 2*(precision_pos * recall_pos) / float(precision_pos + recall_pos)
	sys.stderr.write("fmeasure(positive) = %f\n" % (fmeasure_pos))
