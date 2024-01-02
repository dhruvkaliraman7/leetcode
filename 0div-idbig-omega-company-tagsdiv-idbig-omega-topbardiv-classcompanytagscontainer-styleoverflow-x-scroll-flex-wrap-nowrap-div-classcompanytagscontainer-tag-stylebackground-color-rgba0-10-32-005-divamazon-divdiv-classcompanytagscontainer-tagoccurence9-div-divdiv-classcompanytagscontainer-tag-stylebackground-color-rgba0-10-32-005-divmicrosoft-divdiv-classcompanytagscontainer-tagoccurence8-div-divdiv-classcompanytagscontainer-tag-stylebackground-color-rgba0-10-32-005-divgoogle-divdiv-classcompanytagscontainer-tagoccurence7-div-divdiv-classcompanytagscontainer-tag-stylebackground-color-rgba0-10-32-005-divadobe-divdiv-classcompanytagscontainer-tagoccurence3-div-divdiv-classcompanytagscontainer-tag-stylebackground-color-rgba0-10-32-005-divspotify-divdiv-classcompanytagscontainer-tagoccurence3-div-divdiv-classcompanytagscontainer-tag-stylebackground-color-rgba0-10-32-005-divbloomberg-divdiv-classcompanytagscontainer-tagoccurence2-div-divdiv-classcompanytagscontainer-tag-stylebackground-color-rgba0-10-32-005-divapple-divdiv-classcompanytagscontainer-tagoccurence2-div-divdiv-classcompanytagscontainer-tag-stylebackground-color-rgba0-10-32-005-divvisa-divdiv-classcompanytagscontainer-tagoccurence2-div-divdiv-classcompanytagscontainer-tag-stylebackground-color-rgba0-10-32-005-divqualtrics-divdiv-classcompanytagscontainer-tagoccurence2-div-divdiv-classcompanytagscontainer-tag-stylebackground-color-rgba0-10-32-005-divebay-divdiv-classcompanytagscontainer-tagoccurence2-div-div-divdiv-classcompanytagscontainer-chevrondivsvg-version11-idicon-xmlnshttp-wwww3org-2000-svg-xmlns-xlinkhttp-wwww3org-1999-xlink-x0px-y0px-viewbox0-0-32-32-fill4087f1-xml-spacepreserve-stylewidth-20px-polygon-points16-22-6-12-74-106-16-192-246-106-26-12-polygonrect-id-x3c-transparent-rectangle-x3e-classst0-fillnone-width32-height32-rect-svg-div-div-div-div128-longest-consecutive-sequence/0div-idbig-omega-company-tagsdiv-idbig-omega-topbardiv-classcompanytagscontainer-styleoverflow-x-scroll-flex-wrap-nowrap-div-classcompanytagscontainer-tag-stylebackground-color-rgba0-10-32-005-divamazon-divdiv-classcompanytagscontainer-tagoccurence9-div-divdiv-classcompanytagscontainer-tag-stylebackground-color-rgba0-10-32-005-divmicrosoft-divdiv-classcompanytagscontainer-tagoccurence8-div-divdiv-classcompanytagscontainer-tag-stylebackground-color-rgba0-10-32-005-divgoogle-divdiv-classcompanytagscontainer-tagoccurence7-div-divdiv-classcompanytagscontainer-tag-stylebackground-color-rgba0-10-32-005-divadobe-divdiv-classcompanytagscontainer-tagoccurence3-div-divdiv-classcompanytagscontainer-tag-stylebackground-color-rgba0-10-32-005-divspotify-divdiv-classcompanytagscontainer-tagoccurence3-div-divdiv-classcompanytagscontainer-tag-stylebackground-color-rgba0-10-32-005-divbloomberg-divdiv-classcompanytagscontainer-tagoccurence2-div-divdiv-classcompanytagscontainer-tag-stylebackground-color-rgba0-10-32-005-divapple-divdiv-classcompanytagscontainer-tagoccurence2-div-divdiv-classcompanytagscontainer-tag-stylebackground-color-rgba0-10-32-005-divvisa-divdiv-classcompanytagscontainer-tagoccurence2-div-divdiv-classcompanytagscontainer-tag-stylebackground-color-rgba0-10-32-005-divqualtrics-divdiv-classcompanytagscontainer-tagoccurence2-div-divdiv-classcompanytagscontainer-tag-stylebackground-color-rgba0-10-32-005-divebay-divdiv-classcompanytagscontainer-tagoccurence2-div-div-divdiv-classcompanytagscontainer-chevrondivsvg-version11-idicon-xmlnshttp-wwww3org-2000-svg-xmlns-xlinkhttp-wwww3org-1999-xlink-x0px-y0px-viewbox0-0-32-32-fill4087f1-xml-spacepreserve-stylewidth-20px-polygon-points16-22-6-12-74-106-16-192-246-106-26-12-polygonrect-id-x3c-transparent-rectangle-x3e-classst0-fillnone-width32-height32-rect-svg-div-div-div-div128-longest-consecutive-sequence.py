class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        se=set()
        for n in nums:
            se.add(n)
        maxn=0
        for i,n in enumerate(nums):
            if (n-1) in se:
                continue
            cur_sum=0
            tmp=n
            while tmp in se:
                tmp+=1                
            maxn=max(maxn,tmp-n)
        return maxn
                    