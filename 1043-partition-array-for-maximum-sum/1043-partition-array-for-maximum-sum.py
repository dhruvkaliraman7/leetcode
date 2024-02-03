class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp=[-1 for i in range(len(arr))]
        def dfs(ind):
            if ind>=len(arr):
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            tmp=0
            for i in range(k):
                tmp=max(tmp,len(arr[ind:ind+i+1])*max(arr[ind:ind+i+1])+dfs(ind+i+1))
            dp[ind]= tmp
            return dp[ind]
        return dfs(0)