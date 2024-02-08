class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        cur_sum = 0
        for num in nums:
            if cur_sum + num > num:
                cur_sum = cur_sum+num
            else:
                cur_sum = num
            
            max_sum = max(cur_sum,max_sum)

        return max_sum

        
