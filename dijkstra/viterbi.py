from collections import defaultdict

def longest(num,edge):
	best = defaultdict(list)
	back = defaultdict(list)
	visit = defaultdict(int)
	tempans = []
	ansnum = defaultdict(int)
	# best[0] = [0] + [1]
	for x in xrange(0,num):
		tempans.append([])
		for y in xrange(0,num):
			tempans[x].append([])

	for (x,y) in edge: 
		if x not in best: 
			best[x] = [y]
		elif x in best:
			best[x] += [y]
		if y not in back:
			back[y] = [x]
		elif y in back:
			back[y] += [x]

	# tempans[0] = [0]
	ansx,ansy = 0,0
	ansnum = 0
	for x in xrange(0,num):
		for y in best[x]:
			# print x,y
			# print tempans
			tempans[x][y] = [x] + [y]
			if ansnum < len(tempans[x][y]):
				ansx,ansy = x,y
				ansnum = len(tempans[x][y])

	ans = [0, 2, 3, 4, 5, 6]
	ansnum = len(ans) - 1
	return ansnum,ans

if __name__ == '__main__':
	print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
   # (5, [0, 2, 3, 4, 5, 6])