from collections import defaultdict
# from sys import getrecursionlimit, setrecursionlimit

def match(a,b):
	if  (a,b) == ('A','U') or \
		(a,b) == ('U','A') or \
		(a,b) == ('G','C') or \
		(a,b) == ('C','G') or \
		(a,b) == ('G','U') or \
		(a,b) == ('U','G'):
		return True
	else:
		return False
opt = {}
# totalbest = 0
def best(rna):
	opt = {}
	ans = []
	for x in xrange(0,len(rna)+1):		
		opt[x,x] = 0 ,''
		opt[x,x+1] = 0, '.'
	
	n = len(rna)
	def _best(rna,opt,i,j):
		# totalbest = 0
		# print "i: ",i," j: ",j
		if opt.has_key((i,j)) :
			# print "i: ",i," j: ",j
			# print "find opt = ", opt[i,j] ,'\n'
			return opt[i,j]
		else:
			tempopt = 0,''
			opt1 = _best(rna,opt,i+1,j-1)
			if match(rna[i],rna[j-1]):
				# totalbest += 1
				opt1 = opt1[0]+1, '(' + opt1[1] + ')'
			else:
				opt1 = opt1[0], '.' + opt1[1] + '.'

			
			for k in xrange(i+1,j):
				# print "K: ",k
				opt2a = _best(rna,opt,i,k) #0,1
				# print "opt2a: ", opt2a,'\n'
				opt2b = _best(rna,opt,k,j) #1,2
				# print "opt2b: ", opt2b
				

				if opt2a[0] + opt2b[0] >= tempopt[0] :
					tempopt = opt2a[0] + opt2b[0], opt2a[1] + opt2b[1]
				# print "i: ",i,"k: ", k, "j: ", j, "tempopt: ",tempopt

			opt2 = tempopt
			'''
			print "i: ",i," j: ",j
			print "opt1:" ,opt1
			print "opt2:" ,opt2
			print "opt: ",opt
			'''
			if opt1[0] <= opt2[0] and len(opt2[1]) == j-i:
				opt[0,n] = opt2
				return opt2
			elif len(opt1[1]) == j-i:
				opt[0,n] = opt1
				return opt1

	ans = _best(rna,opt,0,n)
	# print "\nfinal opt: ",opt
	# print totalbest
	return ans

tot = {}
def total(rna):
	return 0
	n = len(rna)
	for x in xrange(0,n+1):		
		tot[x,x] = 0
		tot[x,x+1] = 1
	
	def _total(rna,tot,i,j):
		# setrecursionlimit(10)
		# print "i: ", i, "j: ", j
		# print "tot: ",tot
		if tot.has_key((i,j)):
			return tot[i,j]
		if j-i ==2:
			if match(rna[0],rna[1]):
				tot[i,j] = 2
				return 2
		tot1 = 0
		temptot = 0
		for x in xrange(i+1,j):
			if match(rna[i],rna[x]):
				temptot += 1
		if temptot == 0:
			# print "not first pair"
			tot1 = _total(rna,tot,i+1,j)

		temptot = 0
		tot2 = 0
		for k in xrange(i+1,j+1):  #1,2
			# print "i: ",i, "k: ",k, "j: ",j
			if k-1 < i+1:
				tot2a = _total(rna,tot,i+1,i+1)
			else:
				tot2a = _total(rna,tot,i+1,k-1)
			# print "tot2a: ",tot2a , "i+1: ", i+1, "k-1: ",k
			if k+1 > j:
				tot2b = _total(rna,tot,j,j)
			else:
				tot2b = _total(rna,tot,k+1,j)
			# print "tot2b: ",tot2b ,"k+1: ",k+1, "j: ",j
			# print match(rna[i],rna[k])
			if match(rna[i],rna[k-1]):
				# print "i: ", i,"k: ",k, "j: ", j
				# print "tot2a: ",tot2a ,"i+1: ", i+1, "k-1: ",k-1
				# print "tot2b: ",tot2b ,"k+1: ",k+1, "j: ",j
				if tot2a == 0 or tot2b == 0:
					temptot = tot2a + tot2b + 2
				else:
					temptot = tot2a * 2 * tot2b
			# else:
				# tot2c = _total(rna,tot,k+1,j)
				# tot2d = _total(rna,tot,k+1,j)
				# temptot += tot2a + tot2b
				# temptot = tot2a * tot2b
				# print "temptot: ",temptot
			
			if tot2 < temptot:
				tot2 = temptot 

		# print "tot1: ",tot1
		# print "tot2: ", tot2
		
		if tot1 > tot2:
			# print "set tot1" ,i,j, " = ",tot1 
			tot[i,j] = tot1 
			return tot1 
		else:
			# print "set tot2" ,i,j, " = ",tot2 
			tot[i,j] = tot2 
			return tot2 
		# return tot1 + tot2 +1
	totnum = _total(rna,tot,0,n)
	# print "tot: ",tot 
	return totnum

def kbest(rna, num):
	return []
	# return best(rna)


if __name__ == '__main__':
	s = "ACAGU"
	print s,best(s)
	# print best(s)
	# print best("GCACG")
	# print total("ACAGU")
	# print kbest(s, 10)
   # (2, '((.))')
	s = "AC"
	print s,best(s)
	# print best(s)
	# print total(s)
	# print kbest(s, 10)
	s = "GUAC"
	print s,best(s)
	s = "GCACG"
	print s,best(s)
	s = "CCGG"
	print s,best(s)
	s = "CCCGGG"
	print s,best(s)
	s = "UUCAGGA"
	print s,best(s)
	s = "AUAACCUA"
	print s,best(s)
	s = "UUGGACUUG"
	print s,best(s)
	s = "UUUGGCACUA"
	print s,best(s)
	s = "GAUGCCGUGUAGUCCAAAGACUUC"
	print s,best(s)
	s = "AGGCAUCAAACCCUGCAUGGGAGCG"
	print s,best(s)