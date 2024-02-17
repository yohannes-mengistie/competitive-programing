class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-2
        ans = 0
        while i >-1:
            ans += nums[i]
            i -=2
        return ans
