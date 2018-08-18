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
        else:
            return False
        x = m - 1
        y = 0
        
        while x >= 0 and y < n:
            print matrix[y][x]
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target:
                x -= 1
            else:
                y += 1
        return False
            