class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        j = 0
        count = 0
        cur = 0
        for i in xrange(1,n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                count = 0
                continue
            elif nums[i] == nums[j]:
                count += 1
                if count < 2:
                    j += 1
                    nums[j] = nums[i]
        return j + 1