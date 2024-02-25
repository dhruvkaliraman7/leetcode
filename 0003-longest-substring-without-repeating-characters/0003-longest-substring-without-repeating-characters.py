class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp_set=set()
        j=0
        res=0
        for i,n in enumerate(s):
            # print(i,j,tmp_set)
            tmp_len=len(tmp_set)
            tmp_set.add(n)
            if len(tmp_set)==tmp_len:
                while s[j]!=n:
                    tmp_set.remove(s[j])
                    j+=1
                j+=1
            res=max(res,i-j+1)
        return res
