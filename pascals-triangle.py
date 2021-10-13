class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = []
        for i in range(numRows):
            out = []
            for j in range(i+1):
                if j == 0 or j == i:
                    out.append(1)
                else: 
                    out.append(li[i-1][j-1] + li[i-1][j])
            li.append(out)
        return li
