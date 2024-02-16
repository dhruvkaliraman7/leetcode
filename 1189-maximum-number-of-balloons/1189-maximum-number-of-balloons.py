class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic=defaultdict(int)
        tmp=['b','a','l','o','n']
        count=0
        for ch in text:
            dic[ch]+=1
        minn=float('inf')
        count=0
        for key in dic:
            if key in tmp:
                if key in ['l','o']:
                    minn=min(minn,dic[key]//2)
                else:
                    minn=min(minn,dic[key])
                count+=1
        if count!=5 or minn==float('inf'):
            return 0
        return minn 