import bisect
# Minghung Shih 932 906 326

def find(alist):
	blist=[]
	for i in xrange(len(alist)):
		for y in alist[i+1:]:
			# print "x: ", alist[i], "y: ", y
			target = alist[i] + y
			index = bisect.bisect(alist, target)
			if alist[index-1] == target:
				blist.append([alist[i],y,target])
	return blist
	


if __name__ == '__main__':
	print find([1, 4, 2, 3, 5]) 
	print find([1,4,9,3,0,2,6,8])
	# print find(range(100))

	# returns [(1,3,4), (1,2,3), (1,4,5), (2,3,5)]