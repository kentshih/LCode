class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        n = len(height)
        l, r = 0, n-1
        ans = 0
        minheight = 0
        while l < r:
            while l < r and height[l] <= minheight:
                ans += minheight - height[l]
                l += 1
            while l < r and height[r] <= minheight:
                ans += minheight - height[r]
                r -= 1
            minheight = min(height[l], height[r])
        return ans
                