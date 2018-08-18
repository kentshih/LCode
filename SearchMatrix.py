class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        
        if n > 0:
            m = len(matrix[0])
        x = m - 1
        y = 0
        
        while target != matrix[y][x]:
            if y < n:
                y += 1
            