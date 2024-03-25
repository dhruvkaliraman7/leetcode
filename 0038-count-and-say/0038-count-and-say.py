class Solution:
    def countAndSay(self, n: int) -> str:
        tmp = '1'
        for i in range(2,n+1):
            j = 0
            tmpCount = 0
            newTmp = ''
            while j < len(tmp): 
                charAt = tmp[j]
                tmpCount = 1
                j += 1
                while j < len(tmp) and tmp[j] == charAt:
                    j += 1
                    tmpCount += 1
                newTmp +=(str(tmpCount)+charAt)
            tmp = newTmp
            
        return tmp
                