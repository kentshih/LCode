class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0
        end   = n - 1
        start = 0
        while start <= end:
            mid = ( start + end ) / 2
            if (mid == 0     or nums[mid] >= nums[mid - 1]) and \
               (mid == n - 1 or nums[mid] >= nums[mid + 1]):
                return mid
            elif mid > 0 and nums[mid - 1] > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return mid