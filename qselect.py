#coding=utf-8
# Minghung Shih 932906326
import random
a = [5,3,57,2,2,13,6,6]

def qselect(num,a):
	if len(a) > 0 and num == 0:
		return "input error!"
	if len(a) < num:
		return "search range error!"
	# print "start list: " + `a`
	# print "search num: " + `num`
	if len(a) == num == 1:
		return a[0]
	index = random.randrange(len(a)-1)
	pivot = a[index]
	count = a.count(pivot)
	# print "pivot: " + `pivot`
	left = [x for x in a if x < pivot]
	# print "left: " + `left`
	right = [x for x in a if x > pivot]
	# print "right: " + `right` + "\n"
	if len(left) >= num:
		return qselect(num,left)
	elif len(left) < num:
		if num-count-len(left) <= 0:
			return pivot
		else:
			return qselect(num-len(left)-count,right)
# print qselect(4, a)

