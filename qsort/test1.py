from contextlib import contextmanager
from sys import getrecursionlimit, setrecursionlimit
@contextmanager
def recursionlimit(n=1000):
	rec_limit = getrecursionlimit()
	setrecursionlimit(n)
	yield
	setrecursionlimit(rec_limit)

from qselect import *
# from qsort import *
print qselect(2, [3, 10, 4, 7, 19])
print qselect(4, [11, 2, 8, 3])
print qselect(1, [1, 2, 7, 3, 1, 1, 1, 11, 2, 8, 3])
print qselect(2, [1, 2, 7, 3, 1, 1, 1, 11, 2, 8, 3])
print qselect(3, [1, 2, 7, 3, 1, 1, 1, 11, 2, 8, 3])
print qselect(5, [1, 2, 7, 3, 1, 1, 1, 11, 2, 8, 3])
print qselect(8, [1, 2, 7, 3, 1, 1, 1, 11, 2, 8, 3])
print qselect(500, range(1000))
with recursionlimit(50):
    print qselect(100, range(100))
with recursionlimit(45):
    print qselect(50, range(100))
