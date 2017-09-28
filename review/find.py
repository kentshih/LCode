def find(t,x,best=None):
	if t==[]:
		return best
	left,root,right = t
	if best is None or abs(root - x) < abs(best - x):
		best = root
	if x < root:
		return find(left,x,best)
	return find(right,x,best)

if __name__ == '__main__':
	t = [[[],2,[]],4,[[[],5,[]],6,[[],7,[]]]]
	print find(t,4.7)