class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        count = 0
        for num in nums:
            if num-1 not in hashmap:
                iterator = 0
                while (iterator+num) in hashmap:
                    iterator +=1
                count = max(iterator,count)
        return count

