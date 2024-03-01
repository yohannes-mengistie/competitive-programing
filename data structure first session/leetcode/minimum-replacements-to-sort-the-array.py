class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        replacement = 0
        cur_largest = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < cur_largest:
                cur_largest = nums[i]
                continue
            if nums[i]%cur_largest:
                cur_elements = nums[i] // cur_largest+1
                cur_largest = nums[i]//cur_elements
            else:
                cur_elements = nums[i] // cur_largest
            
            replacement += cur_elements-1
        return replacement