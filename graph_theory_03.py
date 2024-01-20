from collections import deque

class Solution:
    def __init__(self):
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
        self.area = 0
    
    def maxAreaOfIsland(self, grid):
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        result = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if visited[x][y] == False and grid[x][y] == 1:
                    self.area = 0
                    self.dfs(grid, x, y, visited)
                    #self.bfs(grid, x, y, visited)
                    result = max(result, self.area)
        return result
    
    #Depth First Search Function
    def dfs(self, grid, x, y, visited):
        if visited[x][y] or grid[x][y] == 0:
            return
        
        visited[x][y] = True
        self.area += 1
        for i in range(4):
            next_x = x + self.directions[i][0]
            next_y = y + self.directions[i][1]
            
            if next_x < 0 or next_x >= len(grid):
                continue
            if next_y < 0 or next_y >= len(grid[0]):
                continue
            self.dfs(grid, next_x, next_y, visited)
    
    #Breadth First Search Function
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited[x][y] = True
        self.area += 1
        
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + self.directions[i][0]
                next_y = cur_y + self.directions[i][1]
                
                if next_x < 0 or next_x >= len(grid):
                    continue
                if next_y < 0 or next_y >= len(grid[0]):
                    continue
                if visited[next_x][next_y] or grid[next_x][next_y] == 0:
                    continue
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True
                self.area += 1


if __name__ == '__main__':
    #Test data
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    print(Solution().maxAreaOfIsland(grid))