class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        for n in nums:
            dic[n]+=1
        q=[]
        for key in dic:
            q.append([dic[key],key])
        heapq.heapify(q)
        while len(q)>k:
            heapq.heappop(q)
        res=[]
        while q:
            res.append(heapq.heappop(q)[1])
        return res