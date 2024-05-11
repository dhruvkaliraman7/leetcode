class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        lis = []
        for i in range(len(arr)):
            for j in range(i + 1 , len(arr)):
                lis.append([arr[i]/arr[j] , arr[i] , arr[j]])
        heapq.heapify(lis)
        while k > 0:
            tmp = heapq.heappop(lis)
            k -= 1
        return [tmp[1] , tmp[2]]