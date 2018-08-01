class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        for j in range(len(nums2)):
            if i == m - 1:
                nums1 += nums2[j:]
                break
            if nums2[j] < nums1[i]:
                nums1 = nums2[j] + nums1
            
            if