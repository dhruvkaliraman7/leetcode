class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resu=[]
        i=0
        while i <(len(nums)-2):
            while i>0 and nums[i]==nums[i-1] and i <(len(nums)-2):
                i+=1
                continue
            j,k=i+1,len(nums)-1
            target=-nums[i]
            while j<k:
                res=nums[j]+nums[k]
                if res==target:
                    resu.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    
                elif res>target:
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                    
                else:  
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
            i+=1
        return resu
                    