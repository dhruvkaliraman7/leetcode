class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes=0
        lenn=len(nums)
        for i,n in enumerate(nums):
            if n==0:
                zeroes+=1
            else:
                nums[i-zeroes]=nums[i]
        for i in range(zeroes):
            nums[lenn-1-i]=0
        return nums