class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0
        l,r=0, nums[0]
        jump=1
        while r<len(nums)-1:
            tmp_max=nums[l]
            for i in range(l,r+1):
                tmp_max=max(tmp_max, i+nums[i])
            l,r=r+1,tmp_max
            jump+=1
        return jump