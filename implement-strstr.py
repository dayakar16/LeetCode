class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nLn = len(needle)
        if nLn == 0: 
            return 0
        for i in range(len(haystack)-nLn+1):
            win = haystack[i:i+nLn]
            if needle == win:
                return i
        return -1
