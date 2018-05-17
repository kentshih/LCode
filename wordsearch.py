class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n  = len(board), len(board[0])
    def is_valid(self, i, j, board):
        m, n  = len(board), len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return False
        return True

    def dfs(self, i, j, k, visited, board, word):
        if (i, j) in visited:
            return False

        if board[i][j] != word[k]:
            return False

        if k + 1 == len(word):
            return True

        visited.add((i, j))
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if self.is_valid(ni, nj, board) and self.dfs(ni, nj, k+1, visited, board, word):
                return True
        visited.remove((i, j))

        return False

