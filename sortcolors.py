class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = len(nums) - 1
        i = 0
        for x in xrange(j):
            if nums[x] == 1:
                nums[x], nums[x+1] = nums[x+1], nums[x]
        while i != j:
            if nums[i] == 0:
                i += 1
                continue
            if nums[j] == 2:
                j -= 1
                continue
            if nums[i] == 2 or nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                continue
            if nums[i] == 1 and nums[j] == 1:
                break
            