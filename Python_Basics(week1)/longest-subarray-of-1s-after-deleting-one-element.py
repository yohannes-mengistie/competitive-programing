class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        left = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count +=1
            while count > 1:
                if nums[left] == 0:
                    count -=1
                left +=1
            if count !=0:
               ans = max(ans,i-left-count+1)
            else:
                ans = max(ans,i-left-count)

        return ans

            
