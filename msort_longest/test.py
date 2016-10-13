import random
SEED = 13425
random.seed(SEED)

def getrandomlist(n):
    return [random.choice(range(1000)) for _ in xrange(n)]

def sort(a): ## buggy version copied from slides
    if a == []:
        return []
    else:
        pivot = a[0]
        left = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]

from longest import longest
# from solution_longest import longest
print longest([[], 1, []])
print longest([[[], 1, []], 2, [[], 3, []]])
print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
for _ in xrange(7):
    print longest(sort(getrandomlist(random.randint(0,100))))
