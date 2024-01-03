class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic=defaultdict(int)
        for ch in s:
            dic[ch]+=1
        maxn=-1
        for key,val in dic.items():
            if val>1:
                prev=-1
                for i,ch in enumerate(s):
                    if ch==key and prev==-1:
                        prev=i
                        val-=1
                    elif ch==key:
                        val-=1
                        if val==0:
                            maxn=max(maxn,(i-prev-1))
        return maxn
                    