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
            for i in range(numRows):
                k=0 # initial column