class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        def dfs(i,mode):
            if (i,mode) in dp:
                return dp[(i,mode)]
            if i==len(prices):
                return 0
            if mode==0:
                dp[(i,mode)]= max(-prices[i]+dfs(i+1,mode+1),dfs(i+1,mode))
            elif mode==1:
                dp[(i,mode)]= max(prices[i]+dfs(i+1,mode+1),dfs(i+1,mode))
            else:
                dp[(i,mode)]= dfs(i+1,0)
            return dp[(i,mode)]
        return dfs(0,0)