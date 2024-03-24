class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        count = 1
        prev = pairs[0][1]
        # print(pairs)
        for i in range(1,len(pairs)):
            if pairs[i][0] > prev:
                count += 1
                prev= pairs[i][1]
            elif pairs[i][1] < prev:
                prev = pairs[i][1]
        return count