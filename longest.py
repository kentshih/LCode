#coding=utf-8
# Minghung Shih 932906326

def longest(alist):
	leftlong1 = leftlong2 = rightlong1 = rightlong2 = -1
	middlel = middler = 0
	# print "alist: ", alist
	if alist == []:
		return -1
	if alist[0] != []:
		leftlong1 = longest(alist[0][0])
		leftlong2 = longest(alist[0][2])
		middlel = 1
		# print "leftlong1: " , alist[0][0] , "value: ", alist[0][1], "leftlong2: " , alist[0][2]
		# print "value leftlong1: " , leftlong1 , "leftlong2: " , leftlong2

	if alist[2] != []:
		rightlong1 = longest(alist[2][0])
		rightlong2 = longest(alist[2][2])
		middler = 1
		# print "rightlong1: ", alist[2][0], "value: ", alist[2][1],  "rightlong2: ", alist[2][2]
		# print "value rightlong1: " , rightlong1 , "rightlong2: " , rightlong2

	sumlong2 = leftlong1 + leftlong2 + middlel + 1
	sumlong3 = rightlong1 + rightlong2 + middler + 1
	sumlong1 = max(leftlong1,leftlong2) + middlel + middler + 2 + max(rightlong1,rightlong2)
	# print "sum1: ", sumlong1 , "sum2: ", sumlong2, "sum3: ", sumlong3
	return max(sumlong1,sumlong2,sumlong3)

# print longest([[], 1, []])
# print longest([[[], 1, []], 2, [[], 3, []]])
# print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
# print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[[[],10,[[],11,[]]],8,[]], 5, []], 6, [[], 7, [[], 9, [[[],13,[]],12,[]]]]]])
'''
>>> longest([[], 1, []])
   0

   >>> longest([[[], 1, []], 2, [[], 3, []]])
   2

   >>> longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
   5
'''