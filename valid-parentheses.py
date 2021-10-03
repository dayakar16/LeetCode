class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        di = {')':'(', ']':'[','}':'{'}
        for i in range(len(s)): 
            if s[i] == '(' or s[i] == '[' or s[i] == '{': 
                stack.append(s[i])
            else:
                if len(stack) == 0: 
                    return False
                j = stack.pop()
                if j != di[s[i]]:
                    return False
        if len(stack) == 0:     
            return True
        else:
            return False
