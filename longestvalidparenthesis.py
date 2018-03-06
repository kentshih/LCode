class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        tmp = 0
        dp = [0 for x in xrange(len(s))]
        
        for i in xrange(1,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':  # ()()
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':  #(())
                    if dp[i-1] > 0:
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                        dp[i] = 0
                ans = max(ans,dp[i])
        return ans