class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ln = len(nums)
        j = 0
        for i in range(ln): 
            if nums[i]:
                nums[j] = nums[i]
                j += 1
        nums[j:] = [0]*(ln-j)
        
        
