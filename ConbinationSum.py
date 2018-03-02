class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        tmp = 0
        tmpset = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], ans)
        return ans
    
    def dfs(self, candidates, target, index, path, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(path)
            return
        for i in xrange(index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, path + [candidates[i]], ans)
            