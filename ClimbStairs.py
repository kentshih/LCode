class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n)]
        dp[0] = 1
        if n > 1:
            dp[1] = 2
        for i in xrange(2,n):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[-1]