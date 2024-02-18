class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[[] for _ in range(len(nums)+1)]
        dic=defaultdict(int)
        for n in nums:
            dic[n]+=1
        for key in dic:
            res[dic[key]].append(key)
        resn=[]
        for i in range(len(res)-1,-1,-1):
            if res[i]:
                resn.extend(res[i])
                if len(resn)==k:
                    return resn