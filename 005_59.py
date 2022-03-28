class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for i in range(n)]
        
        left = 0
        right = n-1
        up = 0
        down = n-1
        number = 1
        
        while left < right and up < down:
            for x in range(left, right):
                matrix[up][x] = number
                number += 1
            for y in range(up, down):
                matrix[y][right] = number
                number += 1
            for x in range(right, left, -1):
                matrix[down][x] = number
                number += 1    
            for y in range(down, up, -1):
                matrix[y][left] = number
                number += 1
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        if n % 2:
            matrix[n//2][n//2] = number
        
        return matrix

s = Solution()
print(s.generateMatrix(4))
