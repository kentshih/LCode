class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur = nums[0]
        n = len(nums)
        reach = 0
        for i in xrange(n):
            if reach >= i and i+nums[i] > reach:
                reach = i + nums[i]
        return reach >= len(nums) - 1