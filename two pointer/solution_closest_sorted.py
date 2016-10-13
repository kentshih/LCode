import bisect

def find(a, x, k):
    assert k <= len(a), "k shouldn't be larger than n!"
    a = [float("-inf")] + a + [float("inf")]
    place = bisect.bisect(a, x)
    i, j = place-1, place
    for _ in xrange(k):
        if x-a[i] <= a[j]-x:
            i -= 1
        else:
            j += 1
    return a[i+1:j]
