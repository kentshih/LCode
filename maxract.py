class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = 0
        if matrix[0]:
            m = len(matrix[0])
        area = 0
        dp = []
        for row in matrix:
            for x in row:
                if x == 1:
                    area += 1
                
                
        