class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        def isZeroNear(i,j): 
            for a, b in [(i+1,j), (i, j+1), (i-1,j), (i, j-1)]:
                if 0<= a < rows and 0<= b < cols and mat[a][b] == 0:
                    return True
            return False
        
        edges = set()
        for i in range(rows): 
            for j in range(cols): 
                if mat[i][j] == 1 and isZeroNear(i,j):
                    edges.add((i,j,1))          
        visited = set()
        que = edges 
        while que:
            temp = set()
            for i,j,v in que: 
                if (i,j) in visited: 
                    continue
                visited.add((i,j))
                mat[i][j] = v
                for a, b in [(i+1,j), (i, j+1), (i-1,j), (i, j-1)]:
                    if 0<= a < rows and 0<= b < cols and mat[a][b] == 1 and (a,b) not in visited:
                        temp.add((a,b,v+1))
            que = temp
            
        return mat
