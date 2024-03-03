class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        tmp = []
        for x1,x2 in points:
            tmp.append([(x1**2+x2**2)**0.5,x1,x2])
        heapq.heapify(tmp)
        res = []
        while k > 0:
            tmp_val=heapq.heappop(tmp)
            res.append([tmp_val[1],tmp_val[2]])
            k-=1
        return res
        