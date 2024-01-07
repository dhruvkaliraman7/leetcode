class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        dp=[[float('inf') for j in range(26)] for i in range(26)]
        def djistra(dp,start,adj):
            dp[ord(s)-97][ord(s)-97]=0
            q=[(0,start)]
            heapq.heapify(q)
            while q:
                cur_ele=heapq.heappop(q)
                if cur_ele[0]>dp[ord(s)-97][ord(cur_ele[1])-97]:
                    continue
                for ele in adj[cur_ele[1]]:
                    if ele[0]+cur_ele[0]>=dp[ord(s)-97][ord(ele[1])-97]:
                        continue
                    dp[ord(s)-97][ord(ele[1])-97]=ele[0]+cur_ele[0]
                    heapq.heappush(q,(dp[ord(s)-97][ord(ele[1])-97],ele[1]))
            #print('hi')
            
        adj=defaultdict(list)
        for i in range(len(original)):
            adj[original[i]].append((cost[i],changed[i]))
        cost=0
        #print(adj)
        for i,s in enumerate(source):
            if s==target[i]:
                continue
            if dp[ord(s)-97][ord(target[i])-97]==float('inf'):
                djistra(dp,s,adj)
           
            cost+=dp[ord(s)-97][ord(target[i])-97]
            
        return cost if cost!=float('inf') else -1