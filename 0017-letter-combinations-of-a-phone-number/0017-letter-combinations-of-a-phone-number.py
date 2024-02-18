class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        tmp=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        fin=[]
        def dfs(num,ind):
            # print(ind)
            if ind==len(digits):
                fin.append(num)
                return
            # print(tmp[int(digits[ind])-2],num)
            for i in range(len(tmp[int(digits[ind])-2])):
                dfs(num+tmp[int(digits[ind])-2][i],ind+1)
        dfs('',0)
        return fin if fin!=[""] else []