class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        tmpi,tmpj=0,len(nums)-1
        dp={}
        def dfs(i,j,prev_sum):
            # print(i,j,prev_sum)
            if j-i < 1 :
                return 0
            if (i,j,prev_sum) in dp:
                return dp[(i,j,prev_sum)]
            tmp1=tmp2=tmp3=0
            if nums[i] + nums[j] == prev_sum:
                tmp1=  1+ dfs(i+1,j-1,prev_sum)
            if nums[i] + nums[i+1] == prev_sum:
                tmp2= 1+ dfs(i+2,j,prev_sum)
            if nums[j] + nums[j-1] == prev_sum:
                tmp3= 1+ dfs(i,j-2,prev_sum)
            dp[(i,j,prev_sum)]=max(tmp1,tmp2,tmp3)
            return dp[(i,j,prev_sum)]
        return 1+max(dfs(tmpi+2,tmpj,nums[tmpi]+nums[tmpi+1]),dfs(tmpi+1,tmpj-1,nums[tmpi]+nums[tmpj]),dfs(tmpi,tmpj-2,nums[tmpj]+nums[tmpj-1]))