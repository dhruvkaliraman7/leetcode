class Solution:
    def trap(self, height: List[int]) -> int:
        right_traversal,left_traversal=[0]*(len(height)+1),[0]*(len(height)+1)
        for i in range(1,len(height)+1):
            right_traversal[i]=max(height[i-1],right_traversal[i-1])
        for i in range(len(height)-2,-1,-1):
            left_traversal[i]=max(height[i+1],left_traversal[i+1])
        # print(right_traversal,left_traversal
             
        sumn=0
        for i,h in enumerate(height):
            potential=min(right_traversal[i+1],left_traversal[i-1])
            if potential>h:
                sumn+=(potential-height[i])
        return sumn