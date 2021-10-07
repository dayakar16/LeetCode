class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: 
            digits[-1] += 1 
            return digits
        else: 
            i = len(digits) - 1
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i == -1: 
                digits.insert(0,1)
                return digits
            else: 
                digits[i] += 1
                return digits
