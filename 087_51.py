class Solution:
    def __init__(self):
        self.res = []
    
    def solveNQueens(self, n):
        self.res.clear()
        self.board = [['.'] * n for i in range(n)]
        self.backtrack(self.board, 0, n)
        return self.res
    
    def isValid(self, board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    
    def backtrack(self, board, row, n):
        if row == n:
            temp_res = []
            for item in board:
                temp_res.append(''.join(item))
            self.res.append(temp_res)
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            board[row][col] = 'Q'
            self.backtrack(board, row+1, n)
            board[row][col] = '.'

s = Solution()
print(s.solveNQueens(1))
print(s.solveNQueens(3))
print(s.solveNQueens(4))