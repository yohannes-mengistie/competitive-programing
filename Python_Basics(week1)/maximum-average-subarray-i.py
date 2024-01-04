class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0 ; right = k
        
        temp = sum(nums[0:k])
        ma = temp/k
        while right < len(nums):
            
            new = temp-nums[left] + nums[right]
            temp = new
            
            
            ma = max(ma,new/k)
            
            right +=1
            left +=1

        return ma
