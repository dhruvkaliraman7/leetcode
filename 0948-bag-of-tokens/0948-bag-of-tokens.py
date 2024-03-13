class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        maxn , curMax = 0 , 0
        i , j =0, len(tokens)-1
        while i<=j:
            if tokens[i] <= power:
                power -= tokens[i]
                curMax += 1
                i += 1
            elif curMax > 0:
                power += tokens[j]
                curMax -= 1
                j -= 1
            else:
                break
            maxn = max(maxn, curMax)
        return maxn
                