class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixW = min(strs, key= len)
        for i,prefix in enumerate(prefixW): 
            if all(prefixW[:i+1] == st[:i+1] for st in strs):
                continue
            else:
                return prefixW[:i]        
        return prefixW
