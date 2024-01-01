class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        for n in nums:
            dic[n]+=1
        new_dic=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
        print(new_dic)
        res=[]
        for key,val in new_dic.items():
            if k>0:
                res.append(key)
                k-=1
            else:
                return res
        return res