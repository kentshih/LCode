class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        
        ans = 0
        for row in matrix:
            for i in xrange(n):
                height[i] = height[i] + 1 if row[i] == 1 else 0
            stack = [-1]
            for i in xrange(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[i]
                
                if x == 1:
                    area += 1
                
                
        