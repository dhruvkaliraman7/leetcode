class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    #print(res[i],nums[i],nums[j])
                    res[i]=max(res[j]+1,res[i])
        #print(res)
        return max(res)