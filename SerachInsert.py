class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        cur = 0
        stop = False
        while cur < n and nums[cur] < target:
            cur += 1
        
        return cur 
        
        