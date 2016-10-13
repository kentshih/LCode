def _mergesorted((a, numa), (b, numb)):
    if a == [] or b == []:
        return a+b, numa+numb
    c, numc = [], numa+numb
    i, j = 0, 0
    la, lb = len(a), len(b)
    while i < la or j < lb:
        if i == la or (j != lb and a[i] > b[j]):
            c.append(b[j])
            j += 1
            numc += la-i
        else:
            c.append(a[i])
            i += 1
    return c, numc

def _mergesort(lst):
    l = len(lst)
    if l <= 1:
        return lst, 0
    return _mergesorted(_mergesort(lst[:l//2]), _mergesort(lst[l//2:]))

def num_inversions(lst):
    return _mergesort(lst)[1]
