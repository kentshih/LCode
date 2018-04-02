class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0:
            return
        start = 0
        cur = 0
        end = n - 1
        while cur <= end and cur < n:
            if nums[cur] == 0:
                nums[cur], nums[start] = nums[start], 0
                cur += 1
                start += 1
            elif nums[cur] == 1:
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[end] = nums[end], 2
                end -= 1
                
            