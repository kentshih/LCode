class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        cur = msum = nums[0]
        for num in nums[1:]:
            cur = max(num, cur + num)
            msum = max(msum, cur)
        return msum
            
        