class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = 0 ; r=1
        ans = []
        while r < len(nums):
            for i in range(nums[l]):
                ans.append(nums[r])

            l = r+1
            r = l+1
        return ans
