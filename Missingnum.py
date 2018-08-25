class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        if n == 0:
            return 0
        total = n * (n+1) / 2
        
        for x in nums:
            total -= x
        return total