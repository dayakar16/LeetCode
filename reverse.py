class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        st = str(a)[::-1]
        a = int(st)
        if x < 0 and -2**31 < a and a < 2**31: 
            return -a 
        elif x > 0 and -2**31 < a and a < 2**31: 
            return a
        else: 
            return 0
