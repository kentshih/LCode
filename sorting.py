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
    for i in xrange(n):
        
def test():
    seq = list(range(10))
    random.shuffle(seq)
    # bubblesort(seq)
    selectsort(seq)
    assert seq == sorted(seq)

if __name__ == '__main__':
    test()
    