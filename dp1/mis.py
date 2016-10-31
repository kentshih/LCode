# Ming-hung Shih 932-906-326
def _max_wis2(alist):
	if alist==[] or alist == None:
		# print "list is empty!"
		return 0,[]
	# print "list is not empty!"
	max1,max2,temp1 = 0,0,0
	maxlist1,maxlist2,templist1 = {},{},{}

	for x in xrange(0,len(alist)):
		# print "alist: ", alist
		print "x: ",x

		if x == len(alist) - 2:
			# print "last two!"
			max1 = alist[x]
			maxlist1[x] = [alist[x]]
			max2,maxlist2 = _max_wis2(alist[x+1:])

		elif x == len(alist) - 1:
			# print "the last!"
			max1 = alist[x]
			maxlist1[x] = [alist[x]]
			max2 = 0
			maxlist2[x] = []

		elif x < len(alist) -2:
			temp1,templist1 = _max_wis2(alist[x+2:])
			max1= alist[x] + temp1 
			maxlist1 = templist1
			maxlist1[x] = [alist[x]] + maxlist1[x]
			max2,maxlist2 = _max_wis2(alist[x+1:])

		
		if max1 > max2:
			# print "pick ",alist[x]
			return max1,maxlist1
		else:
			# print "not pick ",alist[x]
			return max2,maxlist2

def max_wis2(alist):
	mnum, returnlist = _max_wis2(alist)
	return mnum, returnlist[0]

def _max_wis(alist,num,maxlist):
	maxlist1,maxlist2,templist1 = {},{},{}


	# print "list is not empty!"
	if maxlist.has_key(num):
			return maxlist[num]

	max1,max2,temp1 = 0,0,0
	
	for x in xrange(len(alist)-1,-1,-1):
		print "x: ",x
		if x == len(alist) - 1:
			# print "the last!"
			max1 = alist[x]
			maxlist1[x] = max1,[alist[x]]
			max2 = 0
			maxlist2[x] = 0,[]
			

		elif x == len(alist) - 2:
			# print "last two!"
			max1 = alist[x]
			maxlist1[x] = max1,[alist[x]]
			max2 = alist[x+1]
			maxlist2[x] = alist[x+1], [alist[x+1]]
			# print "maxlist: ",maxlist

		elif x < len(alist) -2:
			temp1,templist1 = _max_wis(alist,x+2,maxlist)
			max1= alist[x] + temp1 
			maxlist1[x] =  max1,[alist[x]] + templist1
			max2 = _max_wis(alist,x+1,maxlist)[0]
			maxlist2[x] = _max_wis(alist,x+1,maxlist)

		if max1 > max2:
			# print "pick ",alist[x]
			maxlist[x] = maxlist1[x]
			# print "maxlist: ",maxlist
			# return max1,maxlist1

		else:
			# print "not pick ",alist[x]
			maxlist[x] = maxlist2[x]
			# print "maxlist: ",maxlist

def max_wis(alist):
	if alist==[] or alist == None:
		# print "list is empty!"
		return 0,[]
	maxlist = {}
	_max_wis(alist,0,maxlist)
	return maxlist[0]

if __name__ == '__main__':
	# print max_wis2([-1,-4,4,6,2,7,1,9,0,2,-3])

	# print max_wis2([5,7,8])
   # (12, [7,5])
	print max_wis([-1,8,10])
   # (10, [10])
	print max_wis([])
   # (0, [])
