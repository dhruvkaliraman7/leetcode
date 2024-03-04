class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        res = 0
        for n in nums:
            if n+k in dic:
                res += dic[n+k]
            if n-k in dic:
                res += dic[n-k]
            dic[n] +=1
        return res                
