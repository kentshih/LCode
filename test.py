from contextlib import contextmanager
from sys import getrecursionlimit, setrecursionlimit
@contextmanager
def recursionlimit(n=1000):
	rec_limit = getrecursionlimit()
	setrecursionlimit(n)
	yield
	setrecursionlimit(rec_limit)

from closest_unsorted import *

print find([1,2,3,4,4,7], 5.2, 2) 
# returns   [4,4]
print find([1,2,3,4,4,7], 6.5, 3) 
# returns   [4,4,7]
print find([4,1,3,2,7,4], 5.2, 2)   
# returns   [4,4]
print find([4,1,3,2,7,4], 6.5, 3)   
# returns   [4,7,4]
print find([4,1,3,2,7,4,6,8], 6.5, 4)
with recursionlimit(50):
    print find(range(10000),47,7)

from xyz import *
with recursionlimit(50):
    print find(range(10))
