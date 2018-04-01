class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        cur = 0
        end = n - 1
        while cur <= end and cur < n:
            
            