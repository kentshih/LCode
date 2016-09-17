class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            dict = target - nums[i]
            if dict in nums and i != nums.index(dict,i):
                return [i,nums.index(dict,i)]
            else:
                continue