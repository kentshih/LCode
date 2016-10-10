import bisect
# Minghung Shih 932 906 326

def find(alist, target, count):
	blist=[]
	p1 = bisect.bisect(alist,target)
	p0 = p1 - 1
	while count != 0:
		# print "count: ", count
		if abs(alist[p1] - target) >= abs(alist[p0] - target):
			num = alist[p0]
			blist.insert(0,num)

			if p0 != 0:
				p0 -= 1
			# print "append ", num
		else:
			num = alist[p1]
			blist.append(num)
			if p1 < len(alist):
				p1 += 1
			# print "insert ", num
		count -= 1
		# print "num: ", num
		# print "index: ", index
	return blist
	


if __name__ == '__main__':
	print find([1,2,3,4,4,6,6], 5, 3)
	# [4,4,6]
	print find([1,2,3,4,4,5,6], 4, 5)
	# [2,3,4,4,5]
	print find(range(1000), 36, 4)