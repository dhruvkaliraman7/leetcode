class Solution:
    def minimumLength(self, s: str) -> int:
        # return 1
        count = len(s)
        i , j = 0 , len(s) - 1
        while s[i] == s[j] and i < j:
            count -= 2
            i += 1
            j -= 1
            while s[i] == s[i-1] and i < j:
                i += 1
                count -= 1
            while s[j] == s[j+1] and j > i:
                j -= 1
                count -= 1
            if i+1 == j and s[i] == s[i+1]:
                return 0
        if i==j:
            if i+1 < len(s):
                if s[i] == s[i+1]:
                    return 0
            elif i-1 > 0:
                if s[i] ==s[i-1]:
                    return 0
        return count