class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in xrange(int(n/2)):
            r = n - 1 - l
            for p in xrange(l, r):
                q = n - 1 - p
                matrix[l][p], matrix[q][l], matrix[r][q], matrix[p][r] = \
                matrix[q][l], matrix[r][q], matrix[p][r], matrix[l][p]
            