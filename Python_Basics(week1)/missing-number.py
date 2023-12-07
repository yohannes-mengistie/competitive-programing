class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] =1
        for val in range(len(nums)+1):
            if val not in hashmap:
                return val