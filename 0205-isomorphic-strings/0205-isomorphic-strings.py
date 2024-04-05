class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        a = set()
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in a:
                    return False
                dic[s[i]] = t[i]
                a.add(t[i])
        return True