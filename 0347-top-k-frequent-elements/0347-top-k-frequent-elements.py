class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        max_n=0
        for n in nums:
            dic[n] += 1
            max_n=max(max_n,dic[n])
        heap = [[] for i in range(max_n+1)]
        for key in dic:
            heap[dic[key]].append(key)
        
        res=[]

        for i in range(max_n,-1,-1):
            if k==0:
                break
            if heap[i]:
                for j in range(len(heap[i])):
                    res.append(heap[i][j])
                    k-=1
        
        return res