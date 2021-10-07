class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: 
            return x 
        
        left = 2 
        right = x // 2 + 1 
        while left <= right: 
            mid = ( left + right ) // 2
            if mid * mid == x: 
                return mid 
            elif mid*mid > x: 
                right = mid -1 
            else: 
                left = mid + 1
        return left-1
