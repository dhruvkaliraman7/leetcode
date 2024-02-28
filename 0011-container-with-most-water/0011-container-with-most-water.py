class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        tmp=0
        while l<r:
            tmp=max(tmp,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return tmp
            