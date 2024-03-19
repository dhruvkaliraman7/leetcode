class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        tmp1 = []
        mi,ma = float('inf'),float('-inf')
        for i,n in enumerate(nums):
            if n[0]< mi:
                mi = n[0]
            if n[0]>ma:
                ma = n[0]
            tmp1.append([n[0],i,0])
        res = [mi,ma]
        heapq.heapify(tmp1)
        while len(tmp1) == len(nums):
            tmp = heapq.heappop(tmp1)
            if len(nums[tmp[1]])>tmp[2]+1:
                if nums[tmp[1]][tmp[2]+1] >ma:
                    ma = nums[tmp[1]][tmp[2]+1]
                heapq.heappush(tmp1,[nums[tmp[1]][tmp[2]+1],tmp[1],tmp[2]+1])
                mi = tmp1[0][0]
                if (ma-mi) < (res[1]-res[0]):
                    res=[mi,ma]
            
        return res
            
            