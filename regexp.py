class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        count = 0
        n = len(s)
        m = len(p)
        table = [[True] + [False]*m]
        for i in xrange(n):
            table.append([False]*(m+1))
        
        for i in xrange(1, n+1):
            cur = p[i-1]
            if cur == '*' and i > 1:
                table[i][0] = table[i-2][0]
            for j in xrange(1, m+1):
                if cur == '*':
                    table[i][j] = table[i-2][j] or \
                                  table[i-1][j] or \
                                 (table[i-1][j-1] and p[i-2] == s[j-1]) or \
                                 (table[i]  [j-1] and p[i-2] == '.' )
                elif cur == '.' or cur == s[j-1]:
                    table[i][j] = table[i-1][j-1]
        return table[n][m]