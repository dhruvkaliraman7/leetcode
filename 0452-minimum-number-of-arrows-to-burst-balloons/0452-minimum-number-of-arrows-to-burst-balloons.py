class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # points.sort(key=lambda x:x[1])
        # res, curEnd = 1, points[0][1]
        # for start,end in points:
        #     if start>curEnd:
        #         curEnd = end
        #         res += 1
        # return res
        points.sort(key = lambda x:x[1])
        count = 1
        start, end = points[0][0],points[0][1]
        for i in range(1,len(points)):
            if points[i][0] <=end:
                start = points[i][0]
            else:
                start = points[i][0]
                end = points[i][1]
                count+=1
        return count