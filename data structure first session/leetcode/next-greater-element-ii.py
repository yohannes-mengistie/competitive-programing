class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1]*len(nums)
        nums = nums+nums
        print(nums)
        for i in range(2*n):
            i = i%(n)
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                ans[index] = nums[i]
            
            stack.append(i)
        print(stack)
        return ans
