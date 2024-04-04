class Solution:
    def maxDepth(self, s: str) -> int:
        tmp = 0
        maxn = 0
        for st in s:
            if st == '(':
                tmp += 1
                maxn = max(maxn, tmp)
            elif st == ')':
                tmp -= 1
        return maxn
                