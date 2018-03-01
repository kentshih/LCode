class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        if n == 0:
            return -1
        cur = n / 2
        for i in xrange(n):
            if nums[i] == target:
                return i