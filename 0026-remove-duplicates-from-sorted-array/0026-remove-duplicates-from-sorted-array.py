class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        prev = 1
        tmpNum = nums[0]
        while i < len(nums):
            if nums[i] == nums[i-1]:
                i+=1
            else:
                nums[prev] = nums[i]
                prev += 1
                i+=1
        return prev