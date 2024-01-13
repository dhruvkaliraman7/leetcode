class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def dfs(ind,sumn):
            if (ind,sumn) in dp:
                return dp[(ind,sumn)]
            if ind==len(nums):
                if sumn==target:
                    return 1
                return 0
            dp[(ind,sumn)]= dfs(ind+1,sumn+nums[ind])+dfs(ind+1,sumn-nums[ind])
            return dp[(ind,sumn)]
        return dfs(0,0)