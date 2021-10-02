class Solution:
    def romanToInt(self, s: str) -> int:
        di = {'I': 1, 'V': 5, 'X': 10, 'L':50,'C': 100, 'D':500, 'M': 1000}
        out = 0 
        for i in range(len(s)):
            out = out + di[s[i]]
            print(out, "outer  ")
            if di[s[i-1]] < di[s[i]] and i != 0:
                out = out - 2*di[s[i-1]]
                print(out, "Inner ")
        return out
