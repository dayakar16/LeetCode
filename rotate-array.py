class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            nums.insert(0,nums[-1])
            nums.pop()
#-------------------------
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = len(nums) - 1 
        ln = len(nums)
        k = k% ln
        nums[:] = nums[ln-k:] + nums[:ln-k]
