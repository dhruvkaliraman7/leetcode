class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l,r=[],[]
        for i,height in enumerate(heights):
            tmp=i-1
            res=1
            while tmp>=0:
                if heights[i]<=heights[tmp]:
                    res+=(l[tmp])
                    tmp-=l[tmp]
                else:
                    break
            l.append(res)
        #print(l)
        r=[1]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            #print(r)
            tmp=i+1
            res=1
            while tmp<len(heights):
                if heights[i]<=heights[tmp]:
                    r[i]+=(r[tmp])
                    tmp+=r[tmp]
                else:
                    break
            
#         for i in range(n - 1, -1, -1):
#             j = i + 1
#             while j < n:
#                 if height[j] >= height[i]:
#                     right[i] += right[j]
#                     j += right[j]
#                 else: break
        max_rect=0
        # print(l)
        # print(r)
        for i,height in enumerate(heights):
            max_rect=max(max_rect,height*(l[i]+r[i]-1))
        return max_rect
    