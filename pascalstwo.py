class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        row = [1]
        for _ in range(numRows):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row