from closest_sorted import find

import signal
import random
random.seed(10)

### random generate some test cases
for i in xrange(4):
    l = [random.randint(0,100) for r in xrange(20)]
    l.sort()
    pivot = random.randint(0,100)
    size = random.randint(4,8)
    print find(l,pivot,size) 
### given test case
print find([1,2,3,4,4,6,6], 5, 3)
print find([1,2,3,4,4,5,6], 4, 5)
print find([1,2,3,4,4,7], 5.2, 2)
print find([1,2,3,4,4,7], 6.5, 3)
### test time complexity
def signal_handler(signum, frame):
    raise Exception("Timed out!")
a = range(1000000)
signal.signal(signal.SIGALRM, signal_handler)
signal.alarm(4)
try:
    print find(a, 1, 1000)
    print find(a, 50000, 3000)
except Exception, msg:
    print "Timed out!"
