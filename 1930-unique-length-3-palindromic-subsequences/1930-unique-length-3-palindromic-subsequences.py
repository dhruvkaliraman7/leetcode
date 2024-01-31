class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic=defaultdict(list)
        res=set()
        for i in range(len(s)):
            dic[s[i]].append(i)
            if len(dic[s[i]])!=1:
                for j in range(dic[s[i]][-2]+1,dic[s[i]][-1]):
                    res.add((s[i],s[j],s[i]))
        resl=len(res)
        for key,val in dic.items():
            if len(val)>=3:
                resl+=1
        return resl