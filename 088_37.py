class Solution:
    def solveSudoku(self, board):
        self.backtrack(board)
        return board
    
    def isValid(self, row, col, val, board):
        for i in range(9):
            if board[row][i] == str(val):
                return False
        for j in range(9):
            if board[j][col] == str(val):
                return False
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row+3):
            for j in range(start_col, start_col+3):
                if board[i][j] == str(val):
                    return False
        return True
    
    def backtrack(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    if self.isValid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtrack(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

s = Solution()
board = [['5','3','.','.','7','.','.','.','.'],
         ['6','.','.','1','9','5','.','.','.'],
         ['.','9','8','.','.','.','.','6','.'],
         ['8','.','.','.','6','.','.','.','3'],
         ['4','.','.','8','.','3','.','.','1'],
         ['7','.','.','.','2','.','.','.','6'],
         ['.','6','.','.','.','.','2','8','.'],
         ['.','.','.','4','1','9','.','.','5'],
         ['.','.','.','.','8','.','.','7','9']]
print(s.solveSudoku(board))