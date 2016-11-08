from collections import defaultdict

def best(cents,value):
   n = len(value)
   back = defaultdict(int)
   def _best(x,i,opt=defaultdict(int)):
      opt[0,n-1] = 0
      if i < 0 or (x, i) in opt:
            return opt[x, i]
      v = value[i]
      xx = x
      while xx > 0:
         j = 1
         ans = _best(xx, i-1) + 1
         if ans > opt[x, i]:
            opt[x, i] = ans
            back[x, i] = j
         xx -= v
         j += 1
      return opt[x, i]
   temp = solution(cents, n-1, back, value)
   if temp == []:
      temp = None
   return _best(cents, n-1), temp

def solution(x, i, back, items):
   if i < 0:
      return []
   j = back[x, i]
   w = items[i]
   return solution(x - w*j, i-1, back, items) + [j]

if __name__ == '__main__':
   print best(47, [6, 10, 15])
   # (3, [2, 2, 1])

   print best(59, [6, 10, 15])
   # (3, [4, 2, 1])	

   print best(37, [4, 6, 15])
   # (3, [4, 1, 1])
 
   print best(27, [4, 6, 15])
   # (2, [3, 0, 1])

   print best(75, [4, 6, 15])
   # (1, [0, 0, 5])

   print best(17, [2, 4, 6])
   # None