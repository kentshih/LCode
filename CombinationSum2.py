class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        n = len(candidates)
        return self.dfs(candidates, 0, [], [], target)
        
    
    def dfs(self, nums, start, res, ans, target):
        n = len(nums)
        if target < 0:
            return
        if target == 0:
            res.append(ans)
            return 
        for i in xrange(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, res, ans+[nums[i]], target - nums[i])
        return res
            