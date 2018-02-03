class Solution(object):
    def getm(target,num):
        if target * 10 % 10 == 0:
            return num[target-1]
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        target = (n+m) / 2.0
        
        if n == 0:
            return nums2[target-1]
        if m == 0:
        start = getm(target,nums1)