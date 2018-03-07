class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = [nums]
        for i in xrange(1, n):
            m = len(ans)
            for k in xrange(m):
                for j in xrange(i):
                    ans.append(ans[k][:])
                    ans[-1][j], ans[-1][i] = ans[-1][i], ans[-1][j]
        return ans