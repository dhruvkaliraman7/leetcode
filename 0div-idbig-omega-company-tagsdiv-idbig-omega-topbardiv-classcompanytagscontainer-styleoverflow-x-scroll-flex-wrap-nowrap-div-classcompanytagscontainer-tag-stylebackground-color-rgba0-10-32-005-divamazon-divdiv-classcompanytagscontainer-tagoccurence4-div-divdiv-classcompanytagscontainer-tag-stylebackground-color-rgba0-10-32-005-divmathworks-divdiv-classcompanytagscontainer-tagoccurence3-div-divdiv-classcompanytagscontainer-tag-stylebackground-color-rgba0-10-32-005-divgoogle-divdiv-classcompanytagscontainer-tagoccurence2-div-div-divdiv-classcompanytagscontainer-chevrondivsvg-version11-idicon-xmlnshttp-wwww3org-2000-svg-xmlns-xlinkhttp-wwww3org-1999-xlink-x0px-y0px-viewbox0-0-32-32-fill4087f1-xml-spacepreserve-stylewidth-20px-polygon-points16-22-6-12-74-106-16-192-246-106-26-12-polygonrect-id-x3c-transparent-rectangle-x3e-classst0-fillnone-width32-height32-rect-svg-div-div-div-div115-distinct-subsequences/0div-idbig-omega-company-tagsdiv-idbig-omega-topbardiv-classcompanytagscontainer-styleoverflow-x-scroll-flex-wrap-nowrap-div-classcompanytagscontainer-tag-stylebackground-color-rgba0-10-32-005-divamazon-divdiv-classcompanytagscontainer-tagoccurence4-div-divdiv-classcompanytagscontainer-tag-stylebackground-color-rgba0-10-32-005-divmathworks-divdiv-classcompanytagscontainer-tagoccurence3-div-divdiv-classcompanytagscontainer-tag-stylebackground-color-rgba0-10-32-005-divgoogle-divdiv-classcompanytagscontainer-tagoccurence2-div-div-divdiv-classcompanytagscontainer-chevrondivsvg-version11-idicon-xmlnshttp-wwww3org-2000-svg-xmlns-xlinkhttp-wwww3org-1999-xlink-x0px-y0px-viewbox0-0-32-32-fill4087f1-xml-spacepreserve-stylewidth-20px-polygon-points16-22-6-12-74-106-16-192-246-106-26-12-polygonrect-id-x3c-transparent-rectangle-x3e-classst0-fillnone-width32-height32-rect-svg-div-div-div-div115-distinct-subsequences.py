class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp={}
        def dfs(ind_s,ind_t):
            if (ind_s,ind_t) in dp:
                return dp[(ind_s,ind_t)]
            if len(t)==ind_t:
                return 1
            if len(s)==ind_s:
                return 0
            if s[ind_s]==t[ind_t]:
                dp[(ind_s,ind_t)]= dfs(ind_s+1,ind_t+1)+dfs(ind_s+1,ind_t)
            else:
                dp[(ind_s,ind_t)]= dfs(ind_s+1,ind_t)
            return dp[(ind_s,ind_t)]
        return dfs(0,0)