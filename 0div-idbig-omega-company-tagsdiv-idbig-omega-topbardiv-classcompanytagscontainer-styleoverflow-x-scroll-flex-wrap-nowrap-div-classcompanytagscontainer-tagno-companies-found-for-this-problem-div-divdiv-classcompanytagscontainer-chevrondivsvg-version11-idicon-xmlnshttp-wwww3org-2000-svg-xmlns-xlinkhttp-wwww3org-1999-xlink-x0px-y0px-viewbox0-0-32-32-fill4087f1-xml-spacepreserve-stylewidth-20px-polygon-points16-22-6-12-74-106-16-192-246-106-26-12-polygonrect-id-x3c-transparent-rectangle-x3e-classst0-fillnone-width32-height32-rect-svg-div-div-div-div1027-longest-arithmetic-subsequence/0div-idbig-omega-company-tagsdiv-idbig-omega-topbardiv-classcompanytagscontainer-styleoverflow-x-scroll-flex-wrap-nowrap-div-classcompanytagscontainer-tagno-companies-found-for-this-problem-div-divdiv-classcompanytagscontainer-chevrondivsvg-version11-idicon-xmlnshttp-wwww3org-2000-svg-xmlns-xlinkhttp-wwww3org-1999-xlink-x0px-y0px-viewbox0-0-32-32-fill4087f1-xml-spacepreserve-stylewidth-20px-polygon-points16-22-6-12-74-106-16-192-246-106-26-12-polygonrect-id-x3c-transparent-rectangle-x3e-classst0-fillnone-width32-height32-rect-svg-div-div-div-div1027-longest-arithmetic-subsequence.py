class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dic={}
        for i in range(len(nums)):
            for position in range(i+1,len(nums)):
                diff=nums[position]-nums[i]
                dic[position,diff]=dic.get((i,diff),1)+1
        return max(dic.values())