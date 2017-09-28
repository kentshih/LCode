
from collections import defaultdict

def order(num, edge):
	best = defaultdict(list)
	back = defaultdict(list)
	visit = defaultdict(int)
	# best[0] = [0] + [1]

	for (x,y) in edge: 
		if x not in best: 
			best[x] = [y]
		elif x in best:
			best[x] += [y]
		if y not in back:
			back[y] = [x]
		elif y in back:
			back[y] += [x]
	ans = []
	for x in xrange(0,10):
		visit[x] = 0
	for x in xrange(0,num): # find order

		for y in back[x]: # back track

			if visit[y] == 0: # not visit, add
				ans += [y]
				visit[y] = 1

			else: #cycle check
				if y in best[x]:
					print y, "cycle!", x
					return None
					
		if visit[x] == 0:
			if best [x] == []:
				for z in back[x]:
					if x in best[z]:
						ans += [x]
						visit[x] = 1
		

	
	print best
	print back
	if len(ans) == num:
		return ans
	else:
		return None	
		


if __name__ == '__main__':
	print order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
   # [0, 1, 2, 3, 4, 5, 6, 7]

   # If we flip the (3,4) edge:

	print order(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])
   # [0, 1, 2, 4, 3, 5, 6, 7]

   # If there is a cycle, output None

	print order(4, [(0,1), (1,2), (2,1), (2,3)])
   # None
