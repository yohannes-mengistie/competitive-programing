class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = {}
        left = 0
        ans = 0
        tot = 0
        for i in range(len(nums)):
            tot +=nums[i]
            if nums[i] not in dic:
                dic[nums[i]] =1
            else:
                dic[nums[i]] +=1

            while dic[nums[i]] >= 2:
                tot -=nums[left]
                dic[nums[left]] -=1
                left +=1

            ans = max(ans,tot)

        return ans
