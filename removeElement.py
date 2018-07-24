class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = []
        j = 0
        for i,x in enumerate(nums):
            if x == val:
                continue
            nums[j] = nums[i]
            j += 1
        return j