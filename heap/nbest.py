# Ming-hung Shih 932-905-326 ONID:shihm

from random import randint
from heapq import heappush, heappop, heapify

def nbesta(a,b):
	assert len(a) == len(b), "different size!"
	length = len(a) 
	sa, sb = sorted(a), sorted(b)
	print sa
	clist = []
	mult = []
	i, j = 0, 0
	for x in sa:
		mult.append([])
		for y in sb:
			mult[i].append(x * y)
			j += 1
		i += 1
	i, j = 0, 0
	while length > 0:
		print "add ", i,j
		print "mult ", mult[i][j]
		clist.append((sa[i],sb[j]))
		mult[i][j] = float('inf')
		minnum = mult[0][0]

		i = i+1 if i+1 < len(sa) else i
		j = j+1 if j+1 < len(sb) else j
		print "i,j: " ,i,j
		for x in xrange(0,i+1):
			for y in xrange(0,i+1):
				if mult[x][y] < minnum:
					minnum = mult[x][y]
					i,j = x,y
		length -= 1
	return clist

def qselect(k, a):
    if a == [] or k < 1 or k > len(a):
        return None
    else:
        pindex = randint(0, len(a)-1)
        a[0],a[pindex] = a[pindex],a[0]
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        lleft = len(left)
        return pivot if k == lleft+1 else \
            qselect(k, left) if k <= lleft else \
            qselect(k-lleft-1, right)


def nbestb(a,b):
	assert len(a) == len(b), "different size!"
	length = len(a) 
	sa, sb = [],[]
	for x in xrange(1,len(a)+1):
		sa.append(qselect(x,a))
	for x in xrange(1,len(b)+1):
		sb.append(qselect(x,b))
	clist = []
	mult = []
	i, j = 0, 0
	for x in sa:
		mult.append([])
		for y in sb:
			mult[i].append(x * y)
			j += 1
		i += 1
	i, j = 0, 0
	while length > 0:
		print "add ", i,j
		print "mult ", mult[i][j]
		clist.append((sa[i],sb[j]))
		mult[i][j] = float('inf')
		minnum = mult[0][0]

		i = i+1 if i+1 < len(sa) else i
		j = j+1 if j+1 < len(sb) else j
		print "i,j: " ,i,j
		for x in xrange(0,i+1):
			for y in xrange(0,i+1):
				if mult[x][y] < minnum:
					minnum = mult[x][y]
					i,j = x,y
		length -= 1
	return clist	

def nbestc(a,b):
	assert len(a) == len(b), "different size!"
	length = len(a) 
	sa, sb = [],[]
	for x in a:
		heappush(sa,x)
	for x in b:
		heappush(sb,x)
	print sa
	clist = []
	mult = []
	i, j = 0, 0
	for x in sa:
		mult.append([])
		for y in sb:
			mult[i].append(x * y)
			j += 1
		i += 1
	i, j = 0, 0
	while length > 0:
		print "add ", i,j
		print "mult ", mult[i][j]
		clist.append((sa[i],sb[j]))
		mult[i][j] = float('inf')
		minnum = mult[0][0]

		i = i+1 if i+1 < len(sa) else i
		j = j+1 if j+1 < len(sb) else j
		print "i,j: " ,i,j
		for x in xrange(0,i+1):
			for y in xrange(0,i+1):
				if mult[x][y] < minnum:
					minnum = mult[x][y]
					i,j = x,y
		length -= 1
	return clist

if __name__ == '__main__':
	alist, blist = [4, 1, 5, 3], [2, 6, 3, 4]
	print nbestc(alist,blist)




