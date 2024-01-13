class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp={}
        def dfs(ind1,ind2):
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]
            if ind1==len(text1) or ind2==len(text2):
                return 0
            if text1[ind1]==text2[ind2]:
                dp[(ind1,ind2)]= 1+dfs(ind1+1,ind2+1)
            else:
                dp[(ind1,ind2)]=max(dfs(ind1+1,ind2),dfs(ind1,ind2+1))
            return dp[(ind1,ind2)]
        return dfs(0,0)
        
        