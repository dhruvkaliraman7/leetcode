class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp={}
        def dfs(ind_1,ind_2):
            if (ind_1,ind_2) in dp:
                return dp[(ind_1,ind_2)]
            if len(word1)==ind_1 and len(word2)!=ind_2:
                return len(word2)-ind_2
            if len(word2)==ind_2:
                if len(word1)==ind_1:
                    return 0
                return len(word1)-ind_1
            if word1[ind_1]==word2[ind_2]:
                dp[(ind_1,ind_2)]= dfs(ind_1+1,ind_2+1)
            else:
                dp[(ind_1,ind_2)]= 1+ min(dfs(ind_1,ind_2+1),dfs(ind_1+1,ind_2),dfs(ind_1+1,ind_2+1))
            return dp[(ind_1,ind_2)]
        return dfs(0,0)