from collections import defaultdict

def lis(astring):
	opt = defaultdict(int)
	ans = defaultdict()
	opt[-1],ans[-1] = float('-inf'), ''
	opt[0] ,ans[0]  = 1, astring[0]
	n=len(astring)
	# opt[n] = (float('inf'),n)
	
	def _lis(i,astring):
		# n = len(astring)
		
		if i < 0 or i in opt:
			# print "call and find ", "i: ",i , " opt: ",opt, "\nans: ",ans, '\n'
			return opt[i],ans[i]

		tempopt1,tempans1 = _lis(i-1,astring)

		# print "start string: ", astring, '\n'
		
		for x in xrange(tempopt1,i):

			# print "x: ",x, "to ", i
			tempopt1,tempans1 = _lis(x,astring)
			# print "current max: ", tempopt1, "ans: ", tempans1
			tempopt3, tempans3 = 1, astring[x-1]
			
			# if tempopt3 <= tempopt1:
			y = x-1
			while y < n-1:
				if tempans3[-1] < astring[y]:
					tempopt3 += 1
					tempans3 = tempans3 + astring[y]
				y += 1
			# print "possible max: ",tempopt3, "ans: ", tempans3

			# if i - tempopt1 >= tempopt1:
			# 	tempopt3, tempans3 = 1, astring[tempopt1]
			# 	print "possible max: ",tempopt3, "ans: ", tempans3

			if tempans3[-1] < astring[x]:
				tempopt3 = tempopt3 + 1
				tempans3 = tempans3 + astring[x]
				# print "new possible max:" ,tempopt3, "ans: ", tempopt3

			tempopt2, tempans2 = 1,astring[x]
			# print "compare ", tempans1[-1], astring[x]
			if tempans1[-1] < astring[x]:

				tempopt2 = tempopt1 + 1
				tempans2 = tempans1 + astring[x]
				# print "find temp1:" ,tempopt1, "temp2: ", tempopt2


			if tempopt3 == tempopt1 and tempans3[-1] < tempans1[-1]:
				tempopt1, tempans1 = tempopt3, tempans3
				# print "possible minimun found!"
				for y in xrange(x-1,-1,-1):
					if ans[y][-1] < tempans3[0]:
						tempopt1 += opt[y]
						tempans1 = ans[y] + tempans3
						
			elif tempopt3 > tempopt1 :
				# print "adjust possible one"
				tempopt1, tempans1 = tempopt3, tempans3

			if tempopt1 < tempopt2:
				# print "new longest find"
				tempopt1, tempans1 = tempopt2, tempans2

			elif tempopt1 == tempopt2:
				# print "adjust small one"
				if tempans1[-1] > tempans2[-1]:
					tempans1 = tempans2


		# print "set i: ", i-1, " opt: ", tempopt1, " ans: ", tempans1, '\n'
		opt[i-1],ans[i-1] = tempopt1, tempans1

		return opt[i-1], ans[i-1]

	return _lis(n,astring)[1]

if __name__ == '__main__':
	print lis("abczabcdefwxabcdefgwz")
	print lis("aebbcg")
   # "abcg"
	print lis("zyx")
   # "z"