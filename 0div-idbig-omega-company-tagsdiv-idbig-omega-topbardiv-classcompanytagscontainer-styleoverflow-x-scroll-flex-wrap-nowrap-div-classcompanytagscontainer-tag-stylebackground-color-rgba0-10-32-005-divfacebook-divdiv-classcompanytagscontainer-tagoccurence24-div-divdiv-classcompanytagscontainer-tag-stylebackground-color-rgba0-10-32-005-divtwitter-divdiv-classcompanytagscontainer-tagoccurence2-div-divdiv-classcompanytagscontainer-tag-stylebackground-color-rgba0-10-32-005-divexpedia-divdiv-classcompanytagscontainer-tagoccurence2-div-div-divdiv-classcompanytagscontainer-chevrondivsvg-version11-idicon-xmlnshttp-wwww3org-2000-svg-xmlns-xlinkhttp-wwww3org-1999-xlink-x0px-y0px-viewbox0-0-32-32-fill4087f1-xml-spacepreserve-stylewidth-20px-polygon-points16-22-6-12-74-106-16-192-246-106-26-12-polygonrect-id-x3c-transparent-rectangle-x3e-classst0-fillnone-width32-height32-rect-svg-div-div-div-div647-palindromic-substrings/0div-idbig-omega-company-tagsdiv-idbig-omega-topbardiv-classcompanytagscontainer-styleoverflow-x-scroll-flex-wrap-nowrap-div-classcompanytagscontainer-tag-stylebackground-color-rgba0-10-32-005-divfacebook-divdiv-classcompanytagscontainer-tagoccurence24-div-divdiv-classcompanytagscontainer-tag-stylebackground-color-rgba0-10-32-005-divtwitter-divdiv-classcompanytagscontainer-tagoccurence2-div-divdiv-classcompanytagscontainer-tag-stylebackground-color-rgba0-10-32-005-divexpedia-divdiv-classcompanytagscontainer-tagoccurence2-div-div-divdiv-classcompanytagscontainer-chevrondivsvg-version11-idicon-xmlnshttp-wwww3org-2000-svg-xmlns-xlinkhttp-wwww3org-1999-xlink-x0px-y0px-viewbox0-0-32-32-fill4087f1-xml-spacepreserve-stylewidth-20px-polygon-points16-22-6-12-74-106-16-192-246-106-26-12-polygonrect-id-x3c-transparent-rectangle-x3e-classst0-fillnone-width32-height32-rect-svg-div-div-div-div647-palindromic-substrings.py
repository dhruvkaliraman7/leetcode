class Solution:
    def countSubstrings(self, s: str) -> int:
        maxn=0
        for i in range(len(s)):
            tmp_str=s[i]
            l,r=i-1,i+1
            maxn+=1
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    tmp_str=s[l]+tmp_str+s[r]
                    l-=1
                    r+=1
                    maxn+=1
                else:
                    break
            
            if i>0 and s[i-1]==s[i]:
                tmp_str=s[i]*2
                l,r=i-2,i+1
                maxn+=1
                while l>=0 and r<len(s):
                    if s[l]==s[r]:
                        tmp_str=s[l]+tmp_str+s[r]
                        l-=1
                        r+=1
                        maxn+=1
                    else:
                        break
                
        return maxn