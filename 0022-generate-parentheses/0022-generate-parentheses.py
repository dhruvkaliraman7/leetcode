class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(l,r,cur):
            if l==0 and r==0:
                res.append(cur)
                return
            if l==0:
                res.append(cur+(')'*r))
                return
            if l==r:
                dfs(l-1,r,cur+'(')
            else:
                dfs(l-1,r,cur+'(')
                dfs(l,r-1,cur+')')
        dfs(n,n,'')
        return res