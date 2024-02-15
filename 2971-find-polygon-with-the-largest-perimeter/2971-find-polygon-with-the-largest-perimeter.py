class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        res=-1
        nums.sort()
        tot=0
        count=0
        for i,num in enumerate(nums):
            if i<2:
                tot+=num
                count+=1
            else:
                if num<tot:
                    res=max(res,tot+num)
                tot+=num
        print(tot)
        return res