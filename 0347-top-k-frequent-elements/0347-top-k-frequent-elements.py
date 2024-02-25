class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        heap = []
        for key , val in dic.items():
            heap.append([-val,key])
        heapq.heapify(heap)
        res=[]
        while k>0:
            tmp=heapq.heappop(heap)
            res.append(tmp[1])
            k-=1
        return res