class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lis=[]
        heapq.heapify(lis)
        heapmax=float('-inf')
        brick_score=0
        for i in range(1,len(heights)):
            
            if heights[i]>heights[i-1]:
                if len(lis)<ladders:
                    heapq.heappush(lis,heights[i]-heights[i-1])
                    heapmax=max(heapmax,heights[i]-heights[i-1])
                else:
                    if ladders>0 and (heights[i]-heights[i-1])>lis[0]:
                        brick_tmp=heapq.heappop(lis)
                        brick_score+=brick_tmp
                        heapq.heappush(lis,heights[i]-heights[i-1])
                        heapmax=max(heapmax,heights[i]-heights[i-1])
                    else:
                        brick_score+=heights[i]-heights[i-1]
                    if brick_score>bricks:
                        return i-1
            # print(lis,brick_score)
                
                    
        
        
        return len(heights)-1