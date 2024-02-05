class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic=defaultdict(int)
        for st in s:
            dic[st]+=1
        for i,st in enumerate(s):
            if dic[st]==1:
                return i
        return -1