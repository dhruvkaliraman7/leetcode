class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[[nums[i]] for i in range(len(nums))]
        res_arr=[]
        for i in range(len(nums)):
            tmp_arr=[]
            for j in range(0,i):
                if nums[i]%nums[j]==0:
                    if len(res[j])>=len(tmp_arr):
                        tmp_arr=res[j]
                    # res[i]=max(res[i],1+res[j])
            res[i].extend(tmp_arr)
            if len(res[i])>len(res_arr):
                res_arr=res[i]
        return res_arr
                
            