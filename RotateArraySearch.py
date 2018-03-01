class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        l = 0
        r = n

        while l < r:
            pivot = (l + r) / 2
            if (nums[0] > target) ^ (nums[0] > nums[pivot]) ^ (target > nums[pivot]):
                l = pivot + 1
            else:
                r = pivot
            
        return l if target in nums[l:l+1] else -1