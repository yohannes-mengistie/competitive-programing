class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        tot = nums[0]
        for i in range(1,len(nums)):
            tot += nums[i]
            cur = ceil(tot/(i+1))
            if cur > res:
                res = cur
        return res