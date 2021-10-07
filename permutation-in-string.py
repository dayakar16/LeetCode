class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        di = Counter(s1)
        print(di)
        ln = len(s1)
        win = s2[:ln]
        di1 = Counter(win)
        if di == di1: 
                return True
        for i in range(len(s2)-ln):
            di1[s2[i]] -= 1 
            if di1[s2[i]] == 0: 
                di1.pop(s2[i])
            if s2[i+ln] in di1: 
                di1[s2[i+ln]] += 1
            else:
                di1[s2[i+ln]] = 1
            if di == di1: 
                return True
        return False
