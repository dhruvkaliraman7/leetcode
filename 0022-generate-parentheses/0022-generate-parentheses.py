class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(left,right,cur_str):
            if left<0 or right<0:
                return
            if left==0 and right==0:
                res.append(cur_str)
                
            if left==right:
                dfs(left-1,right,cur_str+'(')
            if left<right:
                dfs(left-1,right,cur_str+'(')
                dfs(left,right-1,cur_str+')')
        dfs(n,n,'')
        return res