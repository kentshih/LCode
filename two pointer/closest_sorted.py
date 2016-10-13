import bisect
import signal
import random
random.seed(10)
# Minghung Shih 932 906 326

def find(alist, target, count):
	blist=[]
	p1 = bisect.bisect(alist,target)
	if p1 == len(alist):
		p1 -= 1
	p0 = p1 - 1
	
	while count != 0:
		# print "count: ", count
		# print "p1: ", p1 , "p0: ", p0
		if abs(alist[p1] - target) >= abs(alist[p0] - target):
			num = alist[p0]
			blist.insert(0,num)

			if p0 > 0:
				p0 -= 1
			else:
				alist[p0] = float("-inf")
			# print "append ", num
		else:
			num = alist[p1]
			blist.append(num)
			if p1 < len(alist) - 1:
				p1 += 1
			else:
				alist[p1] = float("inf")
			# print "insert ", num
		count -= 1
		# print "num: ", num
		# print "index: ", index
	return blist
	


if __name__ == '__main__':
	for i in xrange(4):
		l = [random.randint(0,100) for r in xrange(20)]
		l.sort()
		print l
		print "len: ", len(l)

		pivot = random.randint(0,100)
		print "pivot: ", pivot
		size = random.randint(4,8)
		print find(l,pivot,size) 
