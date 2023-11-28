class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        forward , backward = 0,len(height)-1
        while forward < backward:
            area = (backward-forward)*min(height[forward],height[backward])
            res =max(res,area)
            if height[forward ]<height[backward]:
                forward +=1
            else :
                backward -=1

        return res