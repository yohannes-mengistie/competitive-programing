class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for ind in range(len(nums)):
            for j in range(ind+1,len(nums)):
                if nums[ind]==nums[j] and (ind*j)%k==0:
                    count +=1

        return count