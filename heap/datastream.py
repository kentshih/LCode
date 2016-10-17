# Ming-hung Shih 932-905-326 ONID:shihm

from heapq import heappush, heappop, heapify
import random

def ksmallest(k,alist):
	# print "alist: ", alist
	minnum = float("-inf")
	count = 0
	index = 0
	heap = []
	result = []
	for x in alist:
		# print "search:" ,x , "minnum: ", minnum
		if count < k:
			heappush(heap,-x)
			if -x >= minnum:
				minnum = heap[0]
			count += 1
			continue
		if -x >= minnum:
			# print "find min: " , x
			if count == k:
				# print "pop: ", heap[0]
				heappop(heap)
				count -= 1
			# heappush(heap,(-x,index))
			heappush(heap,-x)
			# index += 1
			# print "push: ", x
			# print "k: ", heap
			# minnum = heap[0][0]
			minnum = heap[0]
			# print "minnum: ", minnum
			count += 1
				
	while heap != []:
		# result.append(-heappop(heap)[0])
		result.append(-heappop(heap))
	result.sort()
	return result



if __name__ == '__main__':
	# print ksmallest(4, [10, 2, 9, 3, 7, 8, 11, 5, 7])
   # [2, 3, 5, 7]
	# print ksmallest(10, xrange(1000000, 0, -1))
   # [1, 2, 3]
	print ksmallest(10, [random.randint(0,20) for r in xrange(20)])