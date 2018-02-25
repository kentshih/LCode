class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        Mans = ans = 0
        l = 0
        r = n-1
        dp = []
        while l < r:
            left, right = height[l], height[r]
            if left < right:
                ans = (r - l) * left
                while height[l] <= left:
                    l += 1
            
            else:
                ans = (r - l) * right
                while height[r] <= right and r >= 0:
                    r -= 1
            if ans > Mans:
                Mans = ans
        return Mans