class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic_s,dic_t=defaultdict(int),defaultdict(int)
        for i in range(len(s)):
            dic_s[s[i]]+=1
            dic_t[t[i]]+=1
        count=0
        for key_s in dic_s:
            if key_s in dic_t:
                count+=abs(dic_s[key_s]-dic_t[key_s])
            else:
                count+=dic_s[key_s]
        for key_t in dic_t:
            if key_t not in dic_s:
                count+=dic_t[key_t]
        return count//2