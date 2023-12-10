class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}
        for ind,val in enumerate(nums):
            hashmap[val] = ind
        for x,y in operations:
            cur = hashmap[x]
            nums[cur] = y
            hashmap[y] = cur
            del hashmap[x]
        return nums



