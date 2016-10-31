
def fib2(n, cache=None):
	if cache is None:
        cache = {}
    if n in cache:
        return cache[n]         
    print "calculating", n
    cache[n] = 1 if n <= 2 else fib2(n-1, cache) + fib2(n-2, cache)
    return cache[n]


def fib2(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    print "calculating", n
    cache[n] = 1 if n <= 2 else fib2(n-1, cache) + fib2(n-2, cache)
    return cache[n]