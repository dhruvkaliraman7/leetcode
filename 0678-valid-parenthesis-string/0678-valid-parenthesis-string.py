class Solution:
    def checkValidString(self, s: str) -> bool:
        dp={}
        def dfs(ind,score):
            if (ind,score) in dp:
                return dp[(ind,score)]
            if score<0:
                return False
            if ind==len(s) :
                if score!=0:
                    return False
                return True
            if s[ind]=='(':
                dp[(ind,score)] =dfs(ind+1,score+1)
            elif s[ind]==')':
                dp[(ind,score)] =dfs(ind+1,score-1)
            else:
                dp[(ind,score)]= dfs(ind+1,score-1) or dfs(ind+1,score+1) or dfs(ind+1,score)
            return dp[(ind,score)]
        return dfs(0,0)
            