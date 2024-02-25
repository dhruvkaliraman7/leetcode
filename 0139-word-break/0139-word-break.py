class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res=[False for _ in range(len(s)+1)]
        res[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                # print(word)
                # print(s[i:len(word)])
                # if i==0:
                #     print(s[i:i+len(word)])
                #     print(word)
                #     print(res)
                if s[i:i+len(word)]==word:
                    res[i]=res[i+len(word)] or res[i]
        # print(res)
        return res[0]