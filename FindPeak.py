class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0
        end  = n - 1
        start = 0
        while start < end:
            mid = ( start + end ) / 2
            if mid != 0:
                if nums[mid] > nums[mid-1]:
                    
            