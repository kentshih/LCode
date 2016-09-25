#coding=utf-8
import random
a = [5,23,57,2,82,6]

def qselect(num,a):
	# print "list: " + `a`
	if len(a) == num == 1:
		return a[0]
	index = random.randrange(len(a)-1)
	pivot = a[index]
	# print "pivot: " + `pivot`
	left = [x for x in a if x < pivot]
	# print "left: " + `left`
	right = [x for x in a if x > pivot]
	# print "right: " + `right`
	if len(left) >= num:
		# print "new num: " + `num`
		return qselect(num,left)
	elif len(left) < num:
		# print "new num: " + `num-len(left)-1`
		if len(left) == num-1:
			return pivot
		else:
			return qselect(num-len(left)-1,right)
print qselect(4, [11, 2, 8, 3])

