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
        cur = matrix[0]
        
        while target != cur