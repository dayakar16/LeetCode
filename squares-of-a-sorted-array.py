class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0 
        right = len(nums) - 1
        n = right
        out = [0]*(n+1)
        while left <= right: 
            if abs(nums[left]) > abs(nums[right]): 
                out[n] = nums[left]*nums[left]
                n -= 1 
                left += 1
            elif abs(nums[left]) < abs(nums[right]):
                out[n] = nums[right]*nums[right]
                right -= 1 
                n -= 1 
            else:
                out[n] = nums[left]*nums[left]
                left += 1 
                n -= 1 
        return out
