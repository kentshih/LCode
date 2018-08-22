class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        col = 0
        prev = []
        if numRows == 0:
            return ans
        ans += [[1]]
        if numRows == 1:
            return ans
        
        ans += [[1,1]]
        prev = [1,1]
        for i in xrange(2,numRows):
            row = [1,1]
            col = i
            for j in xrange(1,col):
                row = row[:j] + [prev[j-1] + prev[j]] + row[j:]
            prev = row
            ans += [row]
        return ans