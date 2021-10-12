class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # finding the rotten sets
        rows = len(grid)
        cols = len(grid[0])
        rotten = set()
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 2: 
                    rotten.add((i,j,0))
        visited = set()
        que = rotten
        ans = 0
        while que:
            temp = set()
            for i,j,v in que: 
                if (i,j) in visited: 
                    continue
                grid[i][j] = 2
                ans = max(ans,v)
                visited.add((i,j))
                for a,b in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]: 
                    if 0 <= a < rows and 0 <= b < cols and grid[a][b] == 1 and (a,b) not in visited: 
                        temp.add((a,b,v+1))
            que = temp
        for i in range(rows): 
            for j in range(cols): 
                if grid[i][j] == 1:
                    return -1
        return ans
