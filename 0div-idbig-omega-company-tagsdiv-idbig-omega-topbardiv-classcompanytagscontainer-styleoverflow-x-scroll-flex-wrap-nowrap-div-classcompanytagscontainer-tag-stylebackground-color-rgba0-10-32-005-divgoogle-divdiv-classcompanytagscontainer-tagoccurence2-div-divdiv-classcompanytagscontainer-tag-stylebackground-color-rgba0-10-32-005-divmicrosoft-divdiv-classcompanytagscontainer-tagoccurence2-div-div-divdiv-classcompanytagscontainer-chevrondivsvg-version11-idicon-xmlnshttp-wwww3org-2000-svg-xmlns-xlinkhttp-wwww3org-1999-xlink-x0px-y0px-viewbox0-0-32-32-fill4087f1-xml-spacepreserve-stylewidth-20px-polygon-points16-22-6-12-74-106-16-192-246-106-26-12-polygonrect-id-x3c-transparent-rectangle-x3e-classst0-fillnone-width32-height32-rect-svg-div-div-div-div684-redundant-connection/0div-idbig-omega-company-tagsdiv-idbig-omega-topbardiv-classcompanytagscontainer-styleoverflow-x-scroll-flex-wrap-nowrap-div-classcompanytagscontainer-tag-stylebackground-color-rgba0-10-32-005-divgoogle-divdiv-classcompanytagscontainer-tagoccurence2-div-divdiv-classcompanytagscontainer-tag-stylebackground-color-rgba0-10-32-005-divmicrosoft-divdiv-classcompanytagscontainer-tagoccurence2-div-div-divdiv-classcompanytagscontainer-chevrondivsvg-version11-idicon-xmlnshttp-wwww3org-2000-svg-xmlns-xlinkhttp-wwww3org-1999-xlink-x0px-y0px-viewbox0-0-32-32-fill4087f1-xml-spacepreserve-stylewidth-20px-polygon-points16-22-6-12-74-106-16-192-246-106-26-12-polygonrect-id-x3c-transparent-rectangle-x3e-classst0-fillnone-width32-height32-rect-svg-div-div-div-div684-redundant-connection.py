class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        def dfs(node,visit,target):
            if node==target:
                return True
            if node in visit:
                return False
            visit.add(node)
            return any(dfs(neigh,visit,target) for neigh in adj[node])
        for u,v in edges:
            if dfs(u,set(),v):
                return [u,v]
            adj[u].append(v)
            adj[v].append(u)
         