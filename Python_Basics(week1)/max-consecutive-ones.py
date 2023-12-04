class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l =0;r=0
        ma = 0
        while r < len(nums):
            while nums[r]==0 and nums[l]!=0:
               l +=1
            if nums[l] == 0:
                l +=1
            ma = max(ma,r-l+1)
            
            r +=1
                
            
           
        
        return ma
            
