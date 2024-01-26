class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp={}
        if len(s1)+len(s2)!=len(s3):
            return False
        def dfs(one,two):
            if (one,two) in dp:
                return dp[(one,two)]
            if one==len(s1) and two==len(s2):
                return True
            if one==len(s1):
                if s3[one+two:]==s2[two:]:
                    return True
                else:
                    return False
            if two==len(s2):
                if s3[one+two:]==s1[one:]:
                    return True
                else:
                    return False
            if s1[one]==s3[one+two] and s2[two]==s3[one+two]:
                dp[(one,two)]= dfs(one+1,two) or dfs(one,two+1)
            elif s1[one]==s3[one+two]:
                dp[(one,two)]= dfs(one+1,two)
            elif s2[two]==s3[one+two]:
                dp[(one,two)]= dfs(one,two+1)
            else:
                return False
            return dp[(one,two)]
        return dfs(0,0)
                
            