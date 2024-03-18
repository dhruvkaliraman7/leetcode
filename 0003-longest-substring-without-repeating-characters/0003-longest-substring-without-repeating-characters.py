class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        gloLen= 0
        i , j = 0,0
        a= set()
        while i<len(s):
            while s[i] in a:  
                a.remove(s[j])
                j += 1
            a.add(s[i])
            gloLen = max(gloLen, i-j+1)
            i+=1
        return gloLen