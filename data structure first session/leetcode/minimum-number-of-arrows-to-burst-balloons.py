class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        points = sorted(points,key = lambda x: x[1])
        maxima = -float("inf")
        count =0 
        for i in range(len(points)):
            if  maxima < points[i][0]:
                count +=1
                maxima = points[i][1]
        return count
            