class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        print(hashmap)
        for ind,num in enumerate(nums):
            cur = target - num
            if cur in hashmap and ind != hashmap[cur]:
                ans = [ind,hashmap[cur]]
                return ans