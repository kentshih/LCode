class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        one = False
        while n > 0:
            if n & 1:
                if one:
                    return False
                else:
                    one = True
            n >>= 1
        return one