class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        left = 0;right=1;ans =0
        while right < len(points):
            x = points[left]
            y = points[right]
            xx = abs(x[0]-y[0])
            yy = abs(x[1]-y[1])
            ans += (max(xx,yy))
            left +=1
            right +=1
        return ans
