import sys
# Minghung Shih 932 906 326

def getKey(item):
	return item[0]

def find(alist, target, count):
	blist=[]
	while count != 0:
		# print "count: ", count
		num = min(alist, key=lambda x:abs(x-target))
		# print "num: ", num
		index = alist.index(num)
		# print "index: ", index
		blist.append((index,num))
		alist[index] = sys.maxint
		count -= 1
	clist = sorted(blist, key=getKey)
	dlist = []
	for x in clist:
		dlist.append(x[1])
	return dlist
	
	
if __name__ == '__main__':
	a = [4,1,3,2,7,4]
	t = 5.2
	c = 2
	print find([1,2,3,4,4,7], 5.2, 2) 
	# returns   [4,4]
	print find([1,2,3,4,4,7], 6.5, 3) 
    # returns   [4,4,7]