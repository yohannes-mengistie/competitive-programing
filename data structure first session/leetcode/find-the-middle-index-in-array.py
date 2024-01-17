class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = 0 
        right = sum(nums) 
        for ind, num in enumerate(nums): 
            right -= num 
            if left == right:
                return ind 
            left += num
        return -1