class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for j in range(len(nums)):
            r = len(nums)-1
            while j!=r:
                if nums[j] == nums[r]:
                    count +=1
                r -=1
        return count
