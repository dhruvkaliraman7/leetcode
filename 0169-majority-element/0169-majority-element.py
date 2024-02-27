class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        ele=nums[0]
        for i in range(1,len(nums)):
            # print(ele,count)
            if ele == nums[i]:
                count += 1
            else:
                count -= 1
                if count < 0:
                    ele = nums[i]
                    count=1
        return ele