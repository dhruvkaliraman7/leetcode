class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxn=0
        while l<r:
            maxn=max(maxn,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxn