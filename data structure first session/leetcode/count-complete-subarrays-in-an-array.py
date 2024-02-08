class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinict = len(set(nums))
        ans = 0
        for ind in range(len(nums)):
            dic = set()
            for j in range(ind,len(nums)):
                dic.add(nums[j])
                if len(dic) == distinict:
                    ans +=1

        return ans

