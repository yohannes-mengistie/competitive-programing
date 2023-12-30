class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = []
        for x,y in points:
            ans.append(x)

        ans.sort()
        ma = 0
        for ind in range(len(ans)-1):
            cur = ans[ind+1] - ans[ind]
            ma = max(ma,cur)

        return ma

