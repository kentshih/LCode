class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return min(nums[0],nums[1])
        start = 0
        end = n - 1
        while start < end - 1:
            if nums[start] == nums[end]:
                end -= 1
            if nums[mid] > nums[start]:
                end = mid
            elif nums[mid] < nums[start]:
                start = mid