class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        a,b=set(),set()
        mas=set()
        glob=True
        def dfs(ind,a,b):
            if ind in mas:
                return False
            if ind in a:
                for j in range(len(graph[ind])):
                    if graph[ind][j] in a:
                        return True
                    b.add(graph[ind][j])
            elif ind in b:
                for j in range(len(graph[ind])):
                    if graph[ind][j] in b:
                        return True
                    a.add(graph[ind][j])
            mas.add(ind)
            return any(dfs(graph[ind][j],a,b) for j in range(len(graph[ind])))
        
        for i in range(len(graph)):
            if i not in a and i not in b:
                a.add(i)
                if dfs(i,a,b):
                    return False
        return True
                