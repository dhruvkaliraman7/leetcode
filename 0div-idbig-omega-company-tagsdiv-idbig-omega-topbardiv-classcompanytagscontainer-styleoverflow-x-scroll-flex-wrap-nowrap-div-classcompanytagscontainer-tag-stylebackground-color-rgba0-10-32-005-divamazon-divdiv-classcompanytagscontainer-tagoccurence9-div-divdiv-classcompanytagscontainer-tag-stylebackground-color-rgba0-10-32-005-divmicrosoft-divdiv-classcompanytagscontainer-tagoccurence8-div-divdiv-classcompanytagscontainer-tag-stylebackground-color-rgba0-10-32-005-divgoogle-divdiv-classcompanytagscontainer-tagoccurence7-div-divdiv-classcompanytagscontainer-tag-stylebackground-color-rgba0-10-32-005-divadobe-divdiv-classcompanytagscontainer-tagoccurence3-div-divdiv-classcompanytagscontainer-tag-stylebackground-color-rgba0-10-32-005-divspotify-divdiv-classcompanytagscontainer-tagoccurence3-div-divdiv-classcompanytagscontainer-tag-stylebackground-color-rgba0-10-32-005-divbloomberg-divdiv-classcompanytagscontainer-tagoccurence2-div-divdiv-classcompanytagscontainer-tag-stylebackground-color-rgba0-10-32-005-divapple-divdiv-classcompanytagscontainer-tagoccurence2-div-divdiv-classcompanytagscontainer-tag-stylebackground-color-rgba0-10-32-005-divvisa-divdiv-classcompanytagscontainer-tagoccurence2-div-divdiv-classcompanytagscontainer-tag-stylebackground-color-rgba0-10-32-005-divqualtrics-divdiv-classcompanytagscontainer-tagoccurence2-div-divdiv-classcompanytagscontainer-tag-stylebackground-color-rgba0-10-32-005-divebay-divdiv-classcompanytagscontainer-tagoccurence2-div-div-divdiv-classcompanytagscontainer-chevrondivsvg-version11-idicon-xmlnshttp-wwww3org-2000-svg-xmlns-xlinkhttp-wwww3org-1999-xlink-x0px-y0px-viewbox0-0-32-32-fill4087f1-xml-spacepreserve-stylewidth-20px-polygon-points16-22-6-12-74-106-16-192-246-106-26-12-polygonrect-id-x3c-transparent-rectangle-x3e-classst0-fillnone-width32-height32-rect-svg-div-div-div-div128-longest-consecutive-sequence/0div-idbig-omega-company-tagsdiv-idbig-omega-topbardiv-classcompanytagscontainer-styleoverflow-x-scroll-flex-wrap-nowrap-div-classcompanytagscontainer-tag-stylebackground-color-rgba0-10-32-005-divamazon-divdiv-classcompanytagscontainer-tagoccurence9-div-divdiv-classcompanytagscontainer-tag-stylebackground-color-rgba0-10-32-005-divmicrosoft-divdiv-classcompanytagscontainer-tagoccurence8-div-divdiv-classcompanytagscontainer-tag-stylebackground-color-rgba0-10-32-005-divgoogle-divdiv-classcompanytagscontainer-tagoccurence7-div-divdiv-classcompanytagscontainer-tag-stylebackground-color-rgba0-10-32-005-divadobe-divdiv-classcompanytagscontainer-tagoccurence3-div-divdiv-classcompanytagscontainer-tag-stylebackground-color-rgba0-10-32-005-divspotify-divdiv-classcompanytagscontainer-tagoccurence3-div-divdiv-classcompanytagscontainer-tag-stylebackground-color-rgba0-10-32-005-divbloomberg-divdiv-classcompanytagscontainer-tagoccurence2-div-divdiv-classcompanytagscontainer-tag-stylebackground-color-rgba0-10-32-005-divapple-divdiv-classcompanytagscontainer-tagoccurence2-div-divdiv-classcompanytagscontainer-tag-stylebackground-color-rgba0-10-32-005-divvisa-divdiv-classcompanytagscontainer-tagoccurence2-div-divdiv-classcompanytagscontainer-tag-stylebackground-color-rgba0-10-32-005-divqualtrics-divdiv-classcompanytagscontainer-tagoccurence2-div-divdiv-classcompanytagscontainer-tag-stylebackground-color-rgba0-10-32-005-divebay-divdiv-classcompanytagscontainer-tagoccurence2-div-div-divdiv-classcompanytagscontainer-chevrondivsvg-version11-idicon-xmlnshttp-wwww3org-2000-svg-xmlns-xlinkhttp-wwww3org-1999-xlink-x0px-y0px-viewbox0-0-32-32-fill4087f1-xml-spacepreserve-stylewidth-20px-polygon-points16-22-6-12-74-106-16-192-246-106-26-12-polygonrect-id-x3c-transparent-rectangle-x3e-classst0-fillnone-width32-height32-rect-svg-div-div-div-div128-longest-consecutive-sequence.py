class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se=set()
        for n in nums:
            se.add(n)
        maxn=0
        for i,n in enumerate(nums):
            if (n-1) in se:
                continue
            s=True
            cur_sum=0
            while s:
                if n in se:
                    cur_sum+=1
                    n=n+1
                else:
                    break
            maxn=max(maxn,cur_sum)
        return maxn
                    