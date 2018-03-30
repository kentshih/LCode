class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        if n == 0 or m == 0:
            return max(m, n)
        dist = range(m + 1)
        for i in xrange(n):
        
            dist_ij, dist[0] = i, i + 1
            for j in xrange(m):
                if word1[i] == word2[j]:
                    dist_ij, dist[j + 1] = dist[j + 1], dist_ij
                else:
                    dist_ij, dist[j + 1] = dist[j + 1], min(dist[j], dist[j + 1], dist_ij) + 1
        return dist[-1]
                    