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
            return min(nums[0], nums[1])
        start = 0
        end = n - 1
        while start < end - 1:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) / 2
            if (start + end) % 2 == 1:
                mid += 1  
            if nums[start] > nums[mid]:
                end = mid
            elif nums[start] < nums[mid]:
                start = mid
        return min(nums[start],nums[end])