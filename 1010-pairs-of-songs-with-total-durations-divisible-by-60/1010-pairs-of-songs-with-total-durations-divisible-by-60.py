class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = defaultdict(int)
        res = 0
        for t in time:
            if t%60  == 0:
                res += dic[0]  
            elif 60 - t%60 in dic:
                res += dic[60 - t%60]
            dic[t%60] += 1
        return res
        res=0
        # print(dic)
        for k,v in dic.items(): 
            if k==0 or k==30:
                res += (v*(v-1)/2)
            elif (60-k) in dic:
                res += (v*dic[60-k])/2
        return int(res)