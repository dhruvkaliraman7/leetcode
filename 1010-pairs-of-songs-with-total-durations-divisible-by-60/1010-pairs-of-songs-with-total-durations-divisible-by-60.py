class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = defaultdict(int)
        for t in time:
            dic[t%60] += 1
        res=0
        # print(dic)
        for k,v in dic.items(): 
            if k==0 or k==30:
                res += (v*(v-1)/2)
            elif (60-k) in dic:
                res += (v*dic[60-k])/2
        return int(res)