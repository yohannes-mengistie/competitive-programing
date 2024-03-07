class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_height = float("-inf")
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                ind,height = stack.pop()
                max_height = max(max_height,(i-ind)*height)
                start=ind
            stack.append((start,heights[i]))
        for i,h in stack:
            max_height = max(max_height,(len(heights)- i) * h)
        return max_height
