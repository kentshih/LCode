class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        
        dp = [999 for i in xrange(n+1)]
        dp2 = [dp[:] for i in xrange(m+1)]
        if m == 0:
            return n
        if n == 0:
            return m
        dp2[0][0] = 0
        # print dp2
        for i in xrange(1,n+1):
            if word1[i-1] == word2[0]:
                dp2[0][i] = dp2[0][i-1]
            else:
                dp2[0][i] = dp2[0][i-1] + 1
        for j in xrange(1,m+1):
            if word1[0] == word2[j-1]:
                dp2[j][0] = dp2[j-1][0]
            else:
                dp2[j][0] = dp2[j-1][0] + 1
        # print dp2
        for i in xrange(1,n+1):
            for j in xrange(1,m+1):
                
                if word1[i-1] == word2[j-1]:
                    dp2[j][i] = dp2[j-1][i-1]
                else:
                    dp2[j][i] = dp2[j-1][i-1] + 1
                # print i, j
                dp2[j][i] = min(dp2[j-1][i] + 1,dp2[j][i-1] + 1, dp2[j][i])
        print dp2
        return dp2[m][n]
                    