class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0 ; right = len(nums)-1
        count = 0

        while left < right:
            temp = nums[left] + nums[right]
            
            if temp < target:
                count += right-left
                left +=1
            elif temp >= target:
                right -=1

        return count



