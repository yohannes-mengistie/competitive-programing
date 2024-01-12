class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        left = 0
        tot  = 0
        for i in range(len(nums)):
            tot +=nums[i]
             

            while tot >= target:
                tot = tot - nums[left]
                min_len = min(min_len,i-left+1) 
                
                left +=1

            

        if min_len == float("inf"):
            return 0

        else:
           
            return min_len