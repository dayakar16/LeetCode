class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        cols = len(image[0])
        rows = len(image)
        pixel = image[sr][sc]
        que = [(sr,sc)]
        visited = [[False]*cols for _ in range(rows)]
        while que:
            r,c = que.pop(0)
            image[r][c] = newColor
            visited[r][c] = True
            if r+1 < rows and image[r+1][c] == pixel and visited[r+1][c] == False: 
                que.append((r+1,c))
            if c+1 < cols and image[r][c+1] == pixel and visited[r][c+1] == False: 
                que.append((r,c+1))
            if r-1 >=0 and image[r-1][c] == pixel and visited[r-1][c] == False: 
                que.append((r-1,c))
            if c-1 >= 0 and image[r][c-1] == pixel and visited[r][c-1] == False: 
                que.append((r,c-1))
        return image