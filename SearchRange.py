class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return -1,-1
        l = 0
        r = len(nums) - 1
        s = t = 0
        while l < r:
            mid = (l + r) / 2
            
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return -1, -1
        s = l
        l = s
        r = len(nums) - 1
        while l < r:
            mid = (l + r) / 2 + 1
            if nums[mid] == target:
                l = mid
            else:
                r = mid - 1
        t = l
        return s, t
            
                