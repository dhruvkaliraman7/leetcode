class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def dfs(nums):
            one,two=nums[-1],0
            i=len(nums)-2
            while i>=0:
                tmp=one
                one=max(nums[i]+two,one)
                two=tmp
                i-=1
            return max(one,two)
        return max(dfs(nums[1:]),dfs(nums[:-1]))