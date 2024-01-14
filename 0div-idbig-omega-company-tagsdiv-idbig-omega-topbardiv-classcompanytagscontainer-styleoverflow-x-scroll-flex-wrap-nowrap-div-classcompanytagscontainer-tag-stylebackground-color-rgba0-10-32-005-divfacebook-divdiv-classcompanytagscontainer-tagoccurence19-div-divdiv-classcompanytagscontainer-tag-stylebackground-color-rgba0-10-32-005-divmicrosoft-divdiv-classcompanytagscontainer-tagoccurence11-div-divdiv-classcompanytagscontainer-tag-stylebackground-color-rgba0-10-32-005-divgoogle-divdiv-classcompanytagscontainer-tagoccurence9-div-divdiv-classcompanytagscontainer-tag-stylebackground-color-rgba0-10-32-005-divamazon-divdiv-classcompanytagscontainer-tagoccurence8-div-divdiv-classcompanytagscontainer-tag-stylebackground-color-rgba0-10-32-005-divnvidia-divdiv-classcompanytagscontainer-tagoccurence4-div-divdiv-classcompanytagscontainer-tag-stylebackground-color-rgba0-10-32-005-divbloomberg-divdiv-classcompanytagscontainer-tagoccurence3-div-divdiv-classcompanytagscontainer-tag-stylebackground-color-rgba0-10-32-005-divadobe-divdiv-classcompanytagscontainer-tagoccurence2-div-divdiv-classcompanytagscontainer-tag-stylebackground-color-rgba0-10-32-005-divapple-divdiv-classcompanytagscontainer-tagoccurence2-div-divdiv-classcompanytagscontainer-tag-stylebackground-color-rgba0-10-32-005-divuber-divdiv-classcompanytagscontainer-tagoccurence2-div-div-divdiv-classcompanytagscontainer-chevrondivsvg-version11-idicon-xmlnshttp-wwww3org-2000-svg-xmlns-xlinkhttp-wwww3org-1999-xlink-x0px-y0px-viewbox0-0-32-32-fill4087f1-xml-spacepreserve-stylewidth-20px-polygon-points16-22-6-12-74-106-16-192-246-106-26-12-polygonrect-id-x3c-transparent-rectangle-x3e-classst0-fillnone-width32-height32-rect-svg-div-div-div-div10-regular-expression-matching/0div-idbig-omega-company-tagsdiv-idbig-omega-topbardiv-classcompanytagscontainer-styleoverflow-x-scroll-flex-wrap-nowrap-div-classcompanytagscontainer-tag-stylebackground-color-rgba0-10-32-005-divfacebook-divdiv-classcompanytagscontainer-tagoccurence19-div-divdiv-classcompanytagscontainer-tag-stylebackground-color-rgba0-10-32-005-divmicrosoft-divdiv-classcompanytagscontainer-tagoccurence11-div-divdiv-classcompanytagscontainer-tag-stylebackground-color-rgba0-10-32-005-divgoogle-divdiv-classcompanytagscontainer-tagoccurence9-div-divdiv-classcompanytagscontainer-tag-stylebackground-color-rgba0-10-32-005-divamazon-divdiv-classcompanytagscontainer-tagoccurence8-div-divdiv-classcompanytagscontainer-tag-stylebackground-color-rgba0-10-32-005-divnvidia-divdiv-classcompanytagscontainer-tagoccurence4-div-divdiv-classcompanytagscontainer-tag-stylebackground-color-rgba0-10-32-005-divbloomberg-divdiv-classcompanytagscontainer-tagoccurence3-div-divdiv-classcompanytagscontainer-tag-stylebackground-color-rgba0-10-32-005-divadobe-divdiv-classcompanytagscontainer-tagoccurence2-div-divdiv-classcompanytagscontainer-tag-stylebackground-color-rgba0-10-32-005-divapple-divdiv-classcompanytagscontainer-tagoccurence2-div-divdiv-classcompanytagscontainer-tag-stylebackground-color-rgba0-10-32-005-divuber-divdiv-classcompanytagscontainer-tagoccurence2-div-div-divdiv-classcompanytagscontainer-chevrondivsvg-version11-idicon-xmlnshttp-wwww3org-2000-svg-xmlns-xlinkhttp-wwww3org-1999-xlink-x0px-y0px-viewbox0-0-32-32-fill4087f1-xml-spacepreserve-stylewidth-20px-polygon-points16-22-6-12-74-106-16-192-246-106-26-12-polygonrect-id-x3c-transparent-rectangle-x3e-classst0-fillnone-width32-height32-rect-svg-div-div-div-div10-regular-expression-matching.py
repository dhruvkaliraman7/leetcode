class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}
        def dfs(ind_s,ind_p):
            if (ind_s,ind_p) in dp:
                return dp[(ind_s,ind_p)]
            #print(ind_s,ind_p)
            if ind_s>=len(s) and ind_p>=len(p):
                
                return True
            if ind_p>=len(p):
                return False
            if ind_s>=len(s):
                if len(p)-ind_p%2==1:
                    return False
                while ind_p!=len(p):
                    one=p[ind_p]
                    ind_p+=1
                    if ind_p==len(p):
                        return False
                    two=p[ind_p]
                    if two!='*':
                        return False
                    ind_p+=1
                return True
            if ind_p+1 <len(p) and p[ind_p+1]=='*':
                if p[ind_p]=='.':
                    tmp=dfs(ind_s,ind_p+2)
                    i=1
                    while ind_s+i-1<len(s):
                        tmp=tmp or dfs(ind_s+i,ind_p+2)
                        i+=1
                    dp[(ind_s,ind_p)]= tmp
                else:
                    tmp=dfs(ind_s,ind_p+2)
                    i=1
                    while ind_s+i-1<len(s) and s[ind_s+i-1]==p[ind_p]:
                        tmp=tmp or dfs(ind_s+i,ind_p+2)
                        i+=1
                    dp[(ind_s,ind_p)]= tmp
            else:
                if p[ind_p]==s[ind_s] or  p[ind_p]=='.':
                    dp[(ind_s,ind_p)]= dfs(ind_s+1,ind_p+1)
                else:
                    dp[(ind_s,ind_p)]= False
            return dp[(ind_s,ind_p)]
        return dfs(0,0)