class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        runningSum = 0
        sumDictionary = defaultdict(int)
        sumDictionary[0] = 1
        ans = 0
        for i,n in enumerate(nums):
            runningSum += n
            ans += sumDictionary[runningSum - goal]
            sumDictionary[runningSum] += 1
        return ans
