class Solution:
    def rob(self, nums: List[int]) -> int:
        one,two=nums[-1],0
        i=len(nums)-2
        while i>=0:
            tmp=one
            one=max(nums[i]+two,one)
            two=tmp
            i-=1
        return max(one,two)