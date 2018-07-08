import random

def bubblesort(seq):
    n = len(seq)
    for i in xrange(n):
        print seq
        for j in xrange(n-i-1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    print seq

def selectsort(seq):
    n = len(seq)
    for i in xrange(n):
        print seq
        for j in xrange(i,n):
            if seq[j] < seq[i]:
                seq[i], seq[j] = seq[j], seq[i]
    print seq 

def insertsort(seq):
    n = len(seq)
    slist = []
    for i in xrange(n):
        print slist
        if len(slist) == 0:
            slist += [seq[i]]
            continue
        for j in xrange(len(slist)):
            if slist[j] > seq[i]:
                slist = slist[:j] + [seq[i]] + slist[j:]
                break
            if j == len(slist) - 1:
                slist = slist + [seq[i]]
    return slist

def mergesort(seq):
    n = len(seq)
    if n == 1:
        return [seq[0]]
    left = mergesort(seq[:n/2])
    right = mergesort(seq[n/2:])
    # print left, right
    def mergedlist(lseq, rseq):
        nlist = []
        p1 = p2 = 0
        while p1 < len(lseq) and p2 < len(rseq):
            if lseq[p1] < rseq[p2]:
                nlist += [lseq[p1]]
                p1 += 1
            else:
                nlist += [rseq[p2]]
                p2 += 1
        if p1 < len(lseq):
            nlist += lseq[p1:]
        if p2 < len(rseq):
            nlist += rseq[p2:]
        return nlist
    nlist = mergedlist(left, right)
    print nlist
    return nlist
                
def quicksort(seq):
    n = len(seq)
    if n == 0:
        return []
    if n == 1:
        return [seq[0]]
    seq[0], seq[n/2] = seq[n/2], seq[0]
    left = []
    right = []
    for x in seq[1:]:
        if x < seq[0]:
            left += [x]
        else:
            right += [x]
    ans = quicksort(left) + [seq[0]] + quicksort(right)
    print ans
    return ans

        

def test():
    seq = list(range(10))
    random.shuffle(seq)
    # bubblesort(seq)
    # selectsort(seq)
    # seq = insertsort(seq)
    # seq = mergesort(seq)
    seq = quicksort(seq)
    assert seq == sorted(seq)

if __name__ == '__main__':
    test()
    