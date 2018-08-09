class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        start = 0
        ans = 999
        end = n - 1
        while start+1 < end:
            mid = (start + end) / 2
            print start, end
            if nums[start] > nums[mid]:
                end = mid
                continue
            if nums[start] < nums[mid]:
                start = mid
                continue
        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]