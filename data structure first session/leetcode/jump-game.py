class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False
        jump = nums[0]
        for i in range(1,len(nums)-1):
            jump -=1
            if jump < nums[i]:
                jump = nums[i]
            if jump == 0:
                return False
        return True
            

