class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): 
            n = target - nums[i]
            if n in nums: 
                j = nums.index(n)
                if i != j: 
                    return [i,j]
        return []
        
