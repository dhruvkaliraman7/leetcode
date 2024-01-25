class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r,c=len(heights),len(heights[0])
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        self.glo_flag=False
        def dfs(x,y,cur_diff,k):
            #print(x,y,cur_diff,k)
            if x<0 or y<0 or x>=r or y>=c or (x,y) in visit or abs(heights[x][y]-cur_diff)>k:
                return
            if x==r-1 and y==c-1:
                self.glo_flag=True
                return
            visit.add((x,y))
            if not self.glo_flag:
                for new_x,new_y in dirs:
                    dfs(x+new_x,y+new_y,heights[x][y],k)
            return
        l,ri=0,10**6
        while l<ri:
            visit=set()
            mid=(l+ri)//2
            #print(mid)
            dfs(0,0,heights[0][0],mid)
            if self.glo_flag:
                ri=mid
            else:
                l=mid+1
            self.glo_flag=False

        return l
            