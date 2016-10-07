def find(alist, target, count):
	blist=[]
	while count != 0:
		num = min(alist, key=lambda x:abs(x-target))
		index = alist.index(num)
		blist[count] = (num,index)
		alist[index] = sys.maxint
		count -= 1
	sorted(blist)
	

	return blist
	
if __name__ == '__main__':
	a = [4,1,3,2,7,4]
	t = 5.2
	c = 2
	print find(a,t,c)
	print find([4,1,3,2,7,4], 6.5, 3)