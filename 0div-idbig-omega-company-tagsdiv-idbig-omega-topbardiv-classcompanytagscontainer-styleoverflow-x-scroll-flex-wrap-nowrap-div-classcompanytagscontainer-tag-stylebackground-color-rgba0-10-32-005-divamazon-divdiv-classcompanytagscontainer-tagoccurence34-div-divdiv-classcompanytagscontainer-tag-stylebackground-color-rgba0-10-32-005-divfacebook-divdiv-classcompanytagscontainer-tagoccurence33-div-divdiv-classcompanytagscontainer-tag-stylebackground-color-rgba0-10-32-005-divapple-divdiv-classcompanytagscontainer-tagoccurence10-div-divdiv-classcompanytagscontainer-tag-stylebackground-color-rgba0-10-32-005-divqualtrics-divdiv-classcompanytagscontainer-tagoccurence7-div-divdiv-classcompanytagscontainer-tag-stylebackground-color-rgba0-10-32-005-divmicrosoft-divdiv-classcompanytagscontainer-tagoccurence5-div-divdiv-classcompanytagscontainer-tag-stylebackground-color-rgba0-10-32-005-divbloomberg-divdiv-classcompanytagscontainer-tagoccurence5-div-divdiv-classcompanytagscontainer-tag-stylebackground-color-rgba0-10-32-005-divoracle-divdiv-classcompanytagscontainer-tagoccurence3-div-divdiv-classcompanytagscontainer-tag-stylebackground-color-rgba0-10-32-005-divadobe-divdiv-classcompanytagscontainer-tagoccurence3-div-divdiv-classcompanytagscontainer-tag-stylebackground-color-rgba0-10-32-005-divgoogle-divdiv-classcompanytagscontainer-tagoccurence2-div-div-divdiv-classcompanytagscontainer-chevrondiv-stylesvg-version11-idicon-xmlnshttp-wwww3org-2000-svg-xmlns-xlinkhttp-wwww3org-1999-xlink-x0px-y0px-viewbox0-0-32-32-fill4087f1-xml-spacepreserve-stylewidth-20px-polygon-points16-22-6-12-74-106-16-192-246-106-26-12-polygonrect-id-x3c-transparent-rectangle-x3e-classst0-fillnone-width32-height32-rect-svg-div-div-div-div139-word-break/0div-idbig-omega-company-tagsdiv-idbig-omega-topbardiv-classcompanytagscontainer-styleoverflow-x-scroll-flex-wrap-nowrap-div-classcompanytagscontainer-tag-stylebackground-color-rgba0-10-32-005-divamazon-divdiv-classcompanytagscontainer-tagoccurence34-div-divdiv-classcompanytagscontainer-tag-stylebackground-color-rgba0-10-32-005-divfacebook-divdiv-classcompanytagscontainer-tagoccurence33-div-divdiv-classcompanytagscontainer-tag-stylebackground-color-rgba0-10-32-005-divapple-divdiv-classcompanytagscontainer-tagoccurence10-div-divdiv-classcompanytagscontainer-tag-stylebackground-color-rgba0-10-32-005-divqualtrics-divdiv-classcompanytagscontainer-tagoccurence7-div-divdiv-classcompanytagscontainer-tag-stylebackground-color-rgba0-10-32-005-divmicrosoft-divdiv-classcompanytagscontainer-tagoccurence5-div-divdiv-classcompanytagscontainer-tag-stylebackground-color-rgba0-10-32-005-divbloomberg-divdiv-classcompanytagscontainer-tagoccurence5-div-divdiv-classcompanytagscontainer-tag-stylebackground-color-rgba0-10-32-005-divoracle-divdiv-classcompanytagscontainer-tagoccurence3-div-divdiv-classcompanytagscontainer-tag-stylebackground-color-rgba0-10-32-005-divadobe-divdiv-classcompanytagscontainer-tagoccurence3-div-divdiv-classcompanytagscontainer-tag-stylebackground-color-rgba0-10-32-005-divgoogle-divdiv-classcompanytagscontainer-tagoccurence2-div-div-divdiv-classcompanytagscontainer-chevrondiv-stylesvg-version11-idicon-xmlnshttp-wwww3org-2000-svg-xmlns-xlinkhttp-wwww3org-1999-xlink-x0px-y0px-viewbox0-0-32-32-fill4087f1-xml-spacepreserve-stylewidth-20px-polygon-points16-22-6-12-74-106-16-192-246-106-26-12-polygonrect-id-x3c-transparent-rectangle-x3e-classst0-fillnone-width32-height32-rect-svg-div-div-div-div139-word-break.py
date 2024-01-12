class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp={}
        dp[len(s)]=True
        def dfs(index):
            tmp_str=s[index:]
            for word in wordDict:
                flag=True
                for i in range(len(word)):
                    if i>=len(tmp_str):
                        flag=False
                        break
                        
                    if word[i]==tmp_str[i]:
                        continue
                    else:
                        
                        flag=False
                        break
                if flag and index+len(word) in dp and dp[index+len(word)]==True:
                    dp[index]=True
            return
                
            
            
            
        for i in range(len(s)-1,-1,-1):
            dfs(i)
        print(dp)
        if 0 in dp:
            return True
        return False
            