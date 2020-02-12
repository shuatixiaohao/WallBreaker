from collections import deque
class Solution:
    def isValid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x,y) in visited:
            return False
        return grid[x][y] =="1"
    
    def bfs(self, grid,x,y,visited):
        queue = deque([(x,y)])
        visited.add((x,y))
        nei=[(1,0),(-1,0),(0,-1),(0,1)]
        while queue:
            x, y = queue.popleft()
            for dx,dy in nei:
                nextx=x+dx
                nexty=y+dy
                if not self.isValid(grid, nextx, nexty, visited):
                    continue
                queue.append((nextx,nexty))
                visited.add((nextx,nexty))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.bfs(grid,i,j,visited)
                    island+=1
        return island   

