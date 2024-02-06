class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        count=0
        for i in range(len(citations)-1,-1,-1):
            # print(citations[i])
            if citations[i]==0:
                break
            if i<len(citations)-1 and count>=citations[i] and count<=citations[i+1]:
                return count
            count+=1
        return count
            