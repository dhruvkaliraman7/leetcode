class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        grid=defaultdict(list)
        for road in roads:
            grid[road[0]].append(road[1])
            grid[road[1]].append(road[0])
        maxn=0
        for key1 in grid:
            for key2 in grid:
                if key1==key2:
                    continue
                if key1 in grid[key2]:
                    maxn= max(maxn, len(grid[key1])+len(grid[key2])-1)
                else:
                    maxn= max(maxn, len(grid[key1])+len(grid[key2]))
        return maxn
            