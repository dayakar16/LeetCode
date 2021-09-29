class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        maxC = 0
        visited = [[False]*cols for _ in range(rows)]
        
        
        # Dfs algorithm:
        
        def DFS(r,c):
            nonlocal grid
            nonlocal visited
            que = [(r,c)]
            count = 0
            while que:
                r,c = que.pop(0)
                visited[r][c] = True
                count += 1
                print(r,c)
                if r+1 < rows and grid[r+1][c] == 1 and visited[r+1][c] == False: 
                    que.append((r+1,c))
                    visited[r+1][c] = True
                if c+1 < cols and grid[r][c+1] == 1 and visited[r][c+1] == False: 
                    que.append((r,c+1))
                    visited[r][c+1] = True
                if r -1 >= 0 and grid[r-1][c] == 1 and visited[r-1][c] == False: 
                    que.append((r-1,c))
                    visited[r-1][c] = True
                if c-1 >= 0 and grid[r][c-1] == 1 and visited[r][c-1] == False: 
                    que.append((r,c-1))
                    visited[r][c-1] = True
            print(count)
            return count
        
        
        # checking each element whether it is 1 and not before visited and running the DFS algorithm considering each island as graph.
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1 and visited[i][j] == False: 
                    cnt = DFS(i,j)
                    maxC = max(maxC,cnt)
        return maxC

            
            
