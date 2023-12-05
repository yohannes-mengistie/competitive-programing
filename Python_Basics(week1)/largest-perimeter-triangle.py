class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l = 0 ; r=2
        ma = 0
        while r<len(nums):
            cur = nums[l] + nums[l+1]
            if cur > nums[r]:
                ans = sum(nums[l:r+1])
                ma = max(ma,ans)
                
            
            l +=1
            r +=1

        return ma