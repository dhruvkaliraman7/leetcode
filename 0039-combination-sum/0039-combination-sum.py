class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tot = []
        def dfs(i,cur_sum,arr):
            # print(i,cur_sum,arr)
            if cur_sum == target:
                # print('f')
                # print(arr)
                tot.append(arr[:])
                return
            if  cur_sum > target:
                return 
            for j in range(i, len(candidates)):
                arr.append(candidates[j])
                dfs(j , cur_sum + candidates[j], arr)
                arr.pop()
        dfs(0, 0, [])
        return tot
                