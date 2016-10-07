#coding=utf-8
# Minghung Shih 932906326


def merge_sort(lst):
    """Sorts the input list using the merge sort algorithm.

    >>> lst = [4, 5, 1, 6, 3]
    >>> merge_sort(lst)
    [1, 3, 4, 5, 6]
    """
    if len(lst) <= 1:
    	return lst, 0
        # return 0
    mid = len(lst) // 2
    left, spiltleft = merge_sort(lst[:mid])
    right, spiltright = merge_sort(lst[mid:])
    # print "count: " , count
    sortedlist, splits = merge(left, right)
    return sortedlist, splits + spiltleft + spiltright

def merge(left, right):
    """Takes two sorted lists and returns a single sorted list by comparing the
    elements one at a time.

    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    count = 0
    # print "merge: " , `left` , ", " , `right` , ", ", count
    if not left:
    	# print "after merge: " , `left` , ", " , `right` , ", ", count
        return right,0+count
    if not right:
    	# print "after merge: " , `left` , ", " , `right` , ", ", count
        return left,0+count
    if left[0] < right[0]:
        # return [left[0]] + merge(left[1:], right)
        # print "after merge: " , `left` , ", " , `right` , ", ", count
        mergedlist , mergedcount = merge(left[1:], right)
        return [left[0]] + mergedlist ,mergedcount + count
    # return [right[0]] + merge(left, right[1:])
    count += len(left)
    # print "after merge: " , `left` , ", " , `right` , ", ", count
    mergedlist , mergedcount = merge(left, right[1:])
    return [right[0]] + mergedlist , mergedcount + count


def num_inversions(alist):
	"""
	>>> num_inversions([4, 1, 3, 2])
   	4
   	>>> num_inversions([2, 4, 1, 3])
   	3
    """
	blist, spiltans = merge_sort(alist)
	print spiltans
"""
a = [4, 1, 3, 2]
if __name__ == '__main__':

    num_inversions(a)
"""