class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        cur_sum = 0
        dic[0] = -1
        maxn = 0
        for i,n in enumerate(nums):
            if n == 0:
                cur_sum -= 1
            else:
                cur_sum += 1
            if cur_sum in dic:
                maxn = max(maxn, i - dic[cur_sum])
            else:
                dic[cur_sum] = i
        return maxn

