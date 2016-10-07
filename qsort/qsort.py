# Minghung Shih 932906326
def sort(a):
  if a == []:
    return []
  else:
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left), pivot, sort(right)]

def sorted(t):
  print t
def search(t, x):
  print t
def insert(t, x):
  print t
def _search(tree, x):
  print t


tree = sort([4,2,6,3,5,7,1,9])
_search(tree,1)
print tree