class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zero = 0
        max_conscutive = 0
        left = 0 
        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero +=1
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -=1
                left +=1
            max_conscutive = max(max_conscutive,i-left+1)

        return max_conscutive
            
