class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0]
        rightMax = [0]
        for i in range(1,len(height)):
            leftMax.append(max(leftMax[-1],height[i-1]))
        for j in range(len(height)-2 ,-1,-1):
            rightMax.append(max(rightMax[-1],height[j+1]))
        rightMax = sorted(rightMax,reverse =True)
        print(leftMax,rightMax)
        ans = 0
        for i in range(len(height)):
            
            cur = min(leftMax[i],rightMax[i]) - height[i]
            if cur > 0:
                ans += cur
        return ans

