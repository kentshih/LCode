class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [x for i in range(n)]
        dp[0] = 1
        for i in xrange(1,n):
            dp[i] = dp[i-1] + 1
            
        return dp[-1]