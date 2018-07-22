class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        zig_zag =''
        if numRows < 2 or n < numRows: 
            return s
        else:
            for i in xrange(numRows):
                k = 0
                while k < n:
                    if k % (2*numRows - 2) == i:
                        zig_zag += s[k]
                        k += k
                        continue
                    