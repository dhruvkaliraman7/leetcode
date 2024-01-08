class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic=defaultdict(list)
        for i,n in enumerate(manager):
            if n==-1:
                continue
            dic[n].append(i)
        def dfs(cur_cost,cur_manager):
            if informTime[cur_manager]==0:
                return cur_cost
            maxn=float('-inf')
            for sub in dic[cur_manager]:
                maxn=max(maxn, dfs(cur_cost+informTime[cur_manager],sub))
            return maxn
        return dfs(0,headID)
        