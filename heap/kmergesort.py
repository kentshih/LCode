# Ming-hung Shih 932-905-326 ONID:shihm

from heapq import heappush, heappop, heapify

def kmergesort(alist, k):
	if len(alist) <= 1:
		return alist
	head,heapnum = 0, 0
	klist = []
	heapsize = len(alist) // k +1
	print "heapsize: ", heapsize

	# saperate to k-way
	for element in alist:
		if heapnum == 0:
			print "create merge", head
			klist.append([])
		if heapnum != heapsize:
			print "push: ", element
			heappush(klist[head], element)
			heapnum += 1
		if heapnum == heapsize:
			head += 1
			heapnum = 0
		
	# start merge
	result = []
	pop = 0
	while klist != []:
		print "klist: ", klist
		minnum = float("inf")
		for x in klist:
			print "x: ",x
			if x == []:
				pop += 1
				continue
			if x[0] < minnum:
				heapnum = klist.index(x)
				minnum = x[0]
				print "find min! x[0]: ", x[0], "minunum: " , minnum, "heapnum: ", heapnum
		if klist[0] != []:
			print "heapnum: ",heapnum
			result.append(heappop(klist[heapnum]))
			print "result: ", result
		while pop != 0:
			heapify(klist)
			heappop(klist)
			print "POP!!"
			pop -= 1
	return result

if __name__ == '__main__':
	# print kmergesort([4,1,5,2,6,3,7,0], 3) 
	print kmergesort(xrange(1000,0,-2), 1) 