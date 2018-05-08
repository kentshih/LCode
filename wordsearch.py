class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n  = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        return True

        for i in board: