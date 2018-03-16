class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans = 0
        if not m or not n:
            return 0
        cur = [1] * n
        for i in xrange(1, m):
            for j in xrange(1, n):
                cur[j] += cur[j-1]
        return cur[-1]