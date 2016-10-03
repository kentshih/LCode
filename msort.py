#coding=utf-8
# Minghung Shih 932906326
def mergesort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = mergesort(alist[:mid])
    right = mergesort(alist[mid:])
    return merge(left, right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

# print mergesort([4, 2, 5, 1, 6, 3])
