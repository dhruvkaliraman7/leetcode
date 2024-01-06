class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        maxn=float('inf')
        cur_count=0
        cur_sum=0
        while i<=len(nums):
            # print("i: ",i)
            # print("j: ",j)
            # print("cur_count: ",cur_count)
            # print("cur_sum: ",cur_sum)
            if cur_sum>=target:
                maxn=min(maxn,cur_count)
                cur_count-=1
                cur_sum-=nums[j]
                j+=1
            else:
                if i==len(nums):
                    break
                cur_count+=1
                cur_sum+=nums[i]
                i+=1
        return maxn if maxn!=float('inf') else 0